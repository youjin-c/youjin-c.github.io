import asyncio
import os
import re
import random
import time
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import html2text

# md 재작업 필요한 프로젝트 (세션2에서 아직 재스크래핑 안한 것들)
MISSING_PROJECTS = [
    # Main Grid - md 재작업 필요
    "https://youjin.cargo.site/DoodlAR",
    "https://youjin.cargo.site/Toonify",
    "https://youjin.cargo.site/Project-Awkward",
    "https://youjin.cargo.site/Blow-A-Kiss",
    "https://youjin.cargo.site/Object-Segmentation",
    "https://youjin.cargo.site/DICE",
    "https://youjin.cargo.site/One-Zero",
    "https://youjin.cargo.site/Snapchat-Lenses",
    "https://youjin.cargo.site/Face-Recognition-Games",
    "https://youjin.cargo.site/Go-Card",
    "https://youjin.cargo.site/Sigh",
    "https://youjin.cargo.site/Humanphobia",
    # Archive - md 재작업 필요 (이미지 없음)
    "https://youjin.cargo.site/Generative-Music",
    "https://youjin.cargo.site/Game-Design-and-Psychology",
    "https://youjin.cargo.site/Art-Toy-Design",
    "https://youjin.cargo.site/Design-for-Discomfort",
    "https://youjin.cargo.site/Tweet-Reader",
]

# 이미지 다운로드 스킵 여부 (이미 다운로드된 경우 True)
# False로 설정하면 이미지도 다운로드 (기존 파일은 스킵)
SKIP_IMAGE_DOWNLOAD = True  # 이미지는 download_images.py로 이미 다운로드함

# 스크래핑 원본 저장 경로
OUTPUT_ROOT = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective"
# GitHub Pages용 최상단 경로
GITHUB_PAGES_ROOT = "/Users/youjin/Documents/youjin-c.github.io"

async def scrape_project(page, url, output_root):
    """단일 프로젝트 페이지 스크래핑"""

    # URL에서 프로젝트 이름 추출
    project_name = urlparse(url).path.strip("/").replace("/", "-")
    if not project_name:
        project_name = "index"

    print(f"\n{'='*50}")
    print(f"스크래핑 시작: {project_name}")
    print(f"URL: {url}")

    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        # 추가로 2초 대기하여 동적 콘텐츠 로드
        await asyncio.sleep(2)
        html_content = await page.content()
    except Exception as e:
        print(f"ERROR: 페이지 로드 실패 - {e}")
        return False

    soup = BeautifulSoup(html_content, 'html.parser')

    # 이미지 처리
    image_count = 0
    for img_tag in soup.find_all('img', src=True):
        img_url = urljoin(url, img_tag['src'])

        # cargo.site 또는 freight.cargo.site 이미지만
        if 'cargo.site' in img_url and re.match(r'.*\.(jpg|jpeg|png|gif|webp)$', img_url, re.IGNORECASE):
            filename = os.path.basename(urlparse(img_url).path)

            if SKIP_IMAGE_DOWNLOAD:
                # 이미지 스킵: 마크다운용 상대 경로만 업데이트
                relative_path = f"images/{project_name}/{filename}"
                img_tag['src'] = relative_path
                image_count += 1
            else:
                # 이미지 다운로드
                images_dir = os.path.join(output_root, "images", project_name)
                os.makedirs(images_dir, exist_ok=True)

                try:
                    response = await page.request.get(img_url)
                    if response.ok:
                        # 파일명 중복 방지
                        local_path = os.path.join(images_dir, filename)
                        counter = 1
                        while os.path.exists(local_path):
                            name, ext = os.path.splitext(filename)
                            local_path = os.path.join(images_dir, f"{name}_{counter}{ext}")
                            counter += 1

                        with open(local_path, 'wb') as f:
                            f.write(await response.body())

                        # 마크다운용 상대 경로로 업데이트
                        relative_path = f"images/{project_name}/{os.path.basename(local_path)}"
                        img_tag['src'] = relative_path
                        image_count += 1
                        print(f"  이미지 저장: {os.path.basename(local_path)}")
                except Exception as e:
                    print(f"  이미지 다운로드 실패: {img_url} - {e}")

    # HTML -> Markdown 변환
    main_content = str(soup.body) if soup.body else html_content
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    markdown_text = converter.handle(main_content)

    # 마크다운 파일 저장 (markdown/ 폴더에)
    markdown_dir = os.path.join(output_root, "markdown")
    os.makedirs(markdown_dir, exist_ok=True)
    md_path = os.path.join(markdown_dir, f"{project_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    print(f"완료: {project_name}.md (이미지 {image_count}개)")
    return True

async def main():
    print("=" * 60)
    print(f"텍스트 재스크래핑 ({len(MISSING_PROJECTS)}개 프로젝트)")
    print(f"이미지 다운로드: {'스킵' if SKIP_IMAGE_DOWNLOAD else '활성화'}")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        success_count = 0
        for i, url in enumerate(MISSING_PROJECTS):
            if i > 0:
                # 429 에러 방지를 위한 딜레이
                delay = random.uniform(5, 10)
                print(f"\n다음 요청까지 {delay:.1f}초 대기...")
                await asyncio.sleep(delay)

            if await scrape_project(page, url, OUTPUT_ROOT):
                success_count += 1

        await browser.close()

    print("\n" + "=" * 60)
    print(f"완료: {success_count}/{len(MISSING_PROJECTS)} 프로젝트 스크래핑 성공")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
