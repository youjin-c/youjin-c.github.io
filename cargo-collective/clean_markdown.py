#!/usr/bin/env python3
"""
마크다운 파일 정리 스크립트
- 네비게이션 헤더 제거
- 프로젝트 그리드 푸터 제거
- base64 이미지를 로컬 파일로 저장 및 경로 변환
"""

import os
import re
import base64
import hashlib
from pathlib import Path

MARKDOWN_DIR = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective/markdown"
IMAGES_DIR = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective/images"
OUTPUT_DIR = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective/markdown_clean"

# 프로젝트 파일만 처리 (유틸리티 파일 제외)
SKIP_FILES = {
    "Home.md", "Left-Nav.md", "Resume.md", "blog-1.md",
    "index.md", "rss.md", "stylesheet.md",
    "Game-Design-and-The-Psychology-of-Choice.md"  # 중복 파일
}

# 헤더 패턴: 첫 번째 # 타이틀 전까지
HEADER_END_PATTERN = re.compile(r'^# .+', re.MULTILINE)

# 푸터 패턴: 프로젝트 그리드 시작 감지
FOOTER_PATTERNS = [
    r'\[ Fandamonium \]\(/Fandamonium\)',
    r'\[ ColorPiece \]\(/ColorPiece\)',
    r'\[ Emotion Detection \]\(/Emotion-Detection\)',
    r'\[ Smile Filter \]\(/Smile-Filter\)',
    r'\[XR\]\(/XR\)\s*\n\s*\[ ',  # XR 태그 후 프로젝트 링크
    r'\[ML\]\(/ML\).*\n\s*\[ ',   # ML 태그 후 프로젝트 링크
]

# base64 이미지 패턴
BASE64_IMG_PATTERN = re.compile(
    r'!\[([^\]]*)\]\((data:image/([a-zA-Z]+);base64,([A-Za-z0-9+/=]+))\)'
)


def extract_project_name(filename):
    """파일명에서 프로젝트 이름 추출"""
    return filename.replace(".md", "")


def find_header_end(content):
    """헤더 끝 위치 찾기 (첫 번째 # 타이틀)"""
    match = HEADER_END_PATTERN.search(content)
    if match:
        return match.start()
    return 0


def find_footer_start(content):
    """푸터 시작 위치 찾기"""
    # 마지막 수평선(---) 또는 프로젝트 그리드 시작점 찾기

    # 방법 1: 연속된 프로젝트 링크 패턴 찾기
    # [ ProjectName ](/Project-Name) 패턴이 여러 개 연속되면 푸터
    project_link_pattern = re.compile(r'\n\[ [A-Za-z0-9 &\-\*]+ \]\(/[A-Za-z0-9\-]+\)\s*\n')

    matches = list(project_link_pattern.finditer(content))
    if len(matches) >= 3:
        # 연속된 프로젝트 링크가 3개 이상이면 첫 번째를 푸터 시작으로
        # 마지막 몇 개의 매치 중에서 연속된 것 찾기
        for i in range(len(matches) - 2):
            # 현재와 다음 매치 사이에 태그([XR], [ML] 등)만 있는지 확인
            gap = content[matches[i].end():matches[i+1].start()]
            if re.match(r'^\s*\[.*\]\(/.*\)\s*$', gap.strip()) or gap.strip() == '':
                return matches[i].start()

    # 방법 2: 특정 푸터 패턴 찾기
    for pattern in FOOTER_PATTERNS:
        match = re.search(pattern, content)
        if match:
            # 이 패턴 이전의 줄바꿈까지 포함
            start = match.start()
            # 이전 줄바꿈 찾기
            prev_newline = content.rfind('\n\n', 0, start)
            if prev_newline > 0:
                return prev_newline
            return start

    return len(content)


def save_base64_image(base64_data, img_format, project_name, img_index):
    """base64 이미지를 파일로 저장하고 경로 반환"""
    # 이미지 디렉토리 생성
    img_dir = os.path.join(IMAGES_DIR, project_name)
    os.makedirs(img_dir, exist_ok=True)

    # 파일명 생성 (해시 기반으로 중복 방지)
    hash_prefix = hashlib.md5(base64_data.encode()[:100]).hexdigest()[:8]
    filename = f"base64_{img_index}_{hash_prefix}.{img_format}"
    filepath = os.path.join(img_dir, filename)

    # 이미 존재하면 스킵
    if os.path.exists(filepath):
        return f"images/{project_name}/{filename}"

    try:
        img_bytes = base64.b64decode(base64_data)
        with open(filepath, 'wb') as f:
            f.write(img_bytes)
        print(f"  저장: {filename}")
        return f"images/{project_name}/{filename}"
    except Exception as e:
        print(f"  오류: base64 이미지 저장 실패 - {e}")
        return None


def convert_base64_images(content, project_name):
    """base64 이미지를 파일로 변환"""
    img_index = 0

    def replace_base64(match):
        nonlocal img_index
        alt_text = match.group(1)
        img_format = match.group(3).lower()
        base64_data = match.group(4)

        # png, jpeg, gif, webp 지원
        if img_format == 'jpeg':
            img_format = 'jpg'

        new_path = save_base64_image(base64_data, img_format, project_name, img_index)
        img_index += 1

        if new_path:
            return f"![{alt_text}]({new_path})"
        return match.group(0)  # 실패 시 원본 유지

    return BASE64_IMG_PATTERN.sub(replace_base64, content)


def clean_markdown(content, project_name):
    """마크다운 정리"""
    # 1. 헤더 제거
    header_end = find_header_end(content)
    content = content[header_end:]

    # 2. 푸터 제거
    footer_start = find_footer_start(content)
    content = content[:footer_start]

    # 3. base64 이미지 변환
    content = convert_base64_images(content, project_name)

    # 4. 앞뒤 공백 정리
    content = content.strip()

    return content


def process_file(filename):
    """단일 파일 처리"""
    if filename in SKIP_FILES:
        return False

    filepath = os.path.join(MARKDOWN_DIR, filename)
    project_name = extract_project_name(filename)

    print(f"\n처리 중: {filename}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)
    cleaned = clean_markdown(content, project_name)
    new_size = len(cleaned)

    # 출력 디렉토리에 저장
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    reduction = ((original_size - new_size) / original_size) * 100 if original_size > 0 else 0
    print(f"  완료: {original_size:,} → {new_size:,} bytes ({reduction:.1f}% 감소)")

    return True


def main():
    print("=" * 60)
    print("마크다운 정리 스크립트")
    print("=" * 60)

    files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]
    processed = 0

    for filename in sorted(files):
        if process_file(filename):
            processed += 1

    print("\n" + "=" * 60)
    print(f"완료: {processed}개 파일 처리")
    print(f"출력 디렉토리: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
