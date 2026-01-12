#!/usr/bin/env python3
"""
markdown_clean 파일들을 최상단에 적용하는 스크립트
- Front matter가 없는 파일만 교체 (직접 작성한 파일 보존)
- Jekyll front matter 추가
- 이미지 폴더 병합
"""

import os
import shutil
import re

ROOT_DIR = "/Users/youjin/Documents/youjin-c.github.io"
CLEAN_DIR = os.path.join(ROOT_DIR, "cargo-collective/markdown_clean")
CLEAN_IMAGES_DIR = os.path.join(ROOT_DIR, "cargo-collective/images")
ROOT_IMAGES_DIR = os.path.join(ROOT_DIR, "images")

# Front matter가 없는 파일들 (원본 스크래핑 상태) - 이 파일들만 교체
FILES_TO_REPLACE = [
    "Art-Toy-Design.md",
    "Dead-Wood.md",
    "Design-for-Discomfort.md",
    "Detourning-the-Web.md",
    "Game-Design-and-The-Psychology-of-Choice.md",
    "Generative-Music.md",
    "Glitch.md",
    "Habitual-Energy.md",
    "Haptics.md",
    "Humanphobia.md",
    "Machine-Learning-for-the-Web.md",
    "Metabolism.md",
    "SMILE-FACE-IN.md",
    "Sigh-Machine.md",
    "Soft-Sensing.md",
    "Suprememe.md",
    "Swipe.md",
    "The-rest-of-You.md",
    "Thesis.md",
    "Tweequency.md",
    "Tweet-Reader.md",
    "Voice.md",
]

# markdown_clean에만 있는 새 파일들
NEW_FILES = [
    "Sigh.md",
]

def filename_to_title(filename):
    """파일명을 타이틀로 변환"""
    name = filename.replace(".md", "")
    name = name.replace("-", " ")
    # 특수 케이스
    special_cases = {
        "SMILE FACE IN": "Smile Face-in",
        "MOTION RECOGNITION": "Motion Recognition",
        "POSTURE EYE CARE": "Posture & Eye Care",
        "Game Design and The Psychology of Choice": "Game Design and Psychology",
        "Machine Learning for the Web": "Machine Learning for the Web",
        "The rest of You": "The Rest of You",
    }
    return special_cases.get(name, name.title())

def add_front_matter(content, filename):
    """Jekyll front matter 추가"""
    title = filename_to_title(filename)
    front_matter = f"""---
layout: default
title: {title}
---

"""
    return front_matter + content

def process_file(filename):
    """파일 처리: front matter 추가 후 복사"""
    clean_path = os.path.join(CLEAN_DIR, filename)
    root_path = os.path.join(ROOT_DIR, filename)

    if not os.path.exists(clean_path):
        print(f"  ⚠️  {filename} not found in markdown_clean")
        return False

    with open(clean_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Front matter 추가
    new_content = add_front_matter(content, filename)

    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ {filename}")
    return True

def merge_images():
    """이미지 폴더 병합"""
    print("\n이미지 폴더 병합 중...")

    if not os.path.exists(CLEAN_IMAGES_DIR):
        print("  ⚠️  cargo-collective/images 폴더가 없습니다")
        return

    for project_folder in os.listdir(CLEAN_IMAGES_DIR):
        src = os.path.join(CLEAN_IMAGES_DIR, project_folder)
        dst = os.path.join(ROOT_IMAGES_DIR, project_folder)

        if os.path.isdir(src):
            if os.path.exists(dst):
                # 기존 폴더에 파일 추가
                for img_file in os.listdir(src):
                    src_file = os.path.join(src, img_file)
                    dst_file = os.path.join(dst, img_file)
                    if not os.path.exists(dst_file):
                        shutil.copy2(src_file, dst_file)
                        print(f"  + {project_folder}/{img_file}")
            else:
                # 폴더 전체 복사
                shutil.copytree(src, dst)
                print(f"  ✓ {project_folder}/ (새 폴더)")

def main():
    print("=" * 50)
    print("Jekyll 포트폴리오 파일 적용")
    print("=" * 50)

    # 1. 기존 스크래핑 파일 교체
    print("\n1. 원본 스크래핑 파일 교체 (front matter 추가)...")
    for filename in FILES_TO_REPLACE:
        process_file(filename)

    # 2. 새 파일 추가
    print("\n2. 새 파일 추가...")
    for filename in NEW_FILES:
        process_file(filename)

    # 3. 이미지 병합
    merge_images()

    print("\n" + "=" * 50)
    print("완료!")
    print(f"  - 교체된 파일: {len(FILES_TO_REPLACE)}개")
    print(f"  - 새 파일: {len(NEW_FILES)}개")
    print("=" * 50)

if __name__ == "__main__":
    main()
