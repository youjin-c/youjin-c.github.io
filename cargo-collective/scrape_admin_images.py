"""
Admin 페이지에서 프로젝트별 원본 이미지 URL을 추출하고 다운로드하는 스크립트

사용법:
1. Chrome에서 https://youjin.cargo.site/admin 에 로그인
2. 이 스크립트 실행 (Chrome 프로필 사용)
"""

import asyncio
import os
import json
from urllib.parse import urlparse
from playwright.async_api import async_playwright

# Admin에서 가져올 프로젝트 목록
PROJECTS_TO_SCRAPE = [
    # 기존 4개 (라이브에서 받은 이미지 불완전)
    "Swipe",
    "Tweequency",
    "Dead-Wood",
    # 이미지 0개
    "DoodlAR",
    "Toonify",
    "Project-Awkward",
    "Blow-A-Kiss",
    "Object-Segmentation",
    "DICE",
    "One-Zero",
    "Snapchat-Lenses",
    "Face-Recognition-Games",
    "Go-Card",
    "Humanphobia",
]

OUTPUT_ROOT = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective/images"

async def get_project_images(page, project_name):
    """Admin 페이지에서 프로젝트의 이미지 URL들을 추출"""

    # Admin 프로젝트 편집 페이지로 이동
    # URL 패턴: https://youjin.cargo.site/admin/{project_id} 또는 검색으로 찾기
    admin_url = f"https://youjin.cargo.site/{project_name}"

    print(f"\n프로젝트: {project_name}")
    print(f"URL: {admin_url}")

    try:
        await page.goto(admin_url, wait_until="networkidle", timeout=30000)
        await asyncio.sleep(2)

        # 이미지 URL 추출 (Console에서 실행하는 것과 동일)
        urls = await page.evaluate("""
            () => {
                const urls = [];
                document.querySelectorAll('[data-page-images] img').forEach(img => {
                    const original = img.src.replace('/t/thumbnail/w/200/q/75/', '/t/original/');
                    urls.push(original);
                });
                return urls;
            }
        """)

        print(f"  발견된 이미지: {len(urls)}개")
        return urls

    except Exception as e:
        print(f"  에러: {e}")
        return []

async def download_image(page, url, filepath):
    """이미지 다운로드"""
    try:
        response = await page.request.get(url)
        if response.ok:
            with open(filepath, 'wb') as f:
                f.write(await response.body())
            return True
    except Exception as e:
        print(f"    다운로드 실패: {e}")
    return False

async def main():
    print("=" * 60)
    print("Admin 페이지에서 이미지 URL 추출 시도")
    print("=" * 60)

    async with async_playwright() as p:
        # 방법 1: 기존 Chrome 사용자 데이터 사용 시도
        # macOS Chrome 프로필 경로
        user_data_dir = os.path.expanduser("~/Library/Application Support/Google/Chrome")

        try:
            # persistent context로 Chrome 프로필 사용
            context = await p.chromium.launch_persistent_context(
                user_data_dir,
                channel="chrome",  # 설치된 Chrome 사용
                headless=False,    # 디버깅을 위해 브라우저 표시
            )
            page = context.pages[0] if context.pages else await context.new_page()

        except Exception as e:
            print(f"Chrome 프로필 사용 실패: {e}")
            print("일반 브라우저로 시도합니다 (로그인 필요)")

            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context()
            page = await context.new_page()

        # Admin 페이지 접근 테스트
        print("\nAdmin 페이지 접근 테스트...")
        await page.goto("https://youjin.cargo.site/admin", wait_until="networkidle")
        await asyncio.sleep(3)

        # 로그인 상태 확인
        current_url = page.url
        print(f"현재 URL: {current_url}")

        if "login" in current_url.lower() or "signin" in current_url.lower():
            print("\n로그인이 필요합니다!")
            print("브라우저에서 수동으로 로그인해주세요...")
            print("로그인 완료 후 Enter를 누르세요.")
            input()

        # 각 프로젝트의 이미지 추출
        all_results = {}

        for project in PROJECTS_TO_SCRAPE:
            urls = await get_project_images(page, project)
            if urls:
                all_results[project] = urls

                # 이미지 다운로드
                output_dir = os.path.join(OUTPUT_ROOT, project)
                os.makedirs(output_dir, exist_ok=True)

                for i, url in enumerate(urls):
                    filename = os.path.basename(urlparse(url).path)
                    filepath = os.path.join(output_dir, filename)

                    if os.path.exists(filepath):
                        print(f"    [{i+1}/{len(urls)}] 이미 존재: {filename}")
                    else:
                        if await download_image(page, url, filepath):
                            print(f"    [{i+1}/{len(urls)}] 다운로드: {filename}")

                    await asyncio.sleep(1)  # 429 방지

            await asyncio.sleep(2)  # 프로젝트 간 딜레이

        # 결과 저장
        with open("admin_images_result.json", "w") as f:
            json.dump(all_results, f, indent=2)

        print("\n" + "=" * 60)
        print("완료! 결과가 admin_images_result.json에 저장됨")
        print("=" * 60)

        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
