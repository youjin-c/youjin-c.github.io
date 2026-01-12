#!/usr/bin/env python3
"""
Admin 페이지 로그인 후 CargoCollective 포트폴리오 스크래이핑 스크립트
랜덤 딜레이를 추가하여 봇으로 의심받지 않도록 함
"""

import asyncio
import os
import re
import random
import time
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import html2text

# 로그인 정보
ADMIN_EMAIL = "elqtfy@gmail.com"
ADMIN_PASSWORD = "YiVCLgZLe2CP6v-"
ADMIN_URL = "https://youjin.cargo.site/admin"

# 랜덤 딜레이 설정 (초)
MIN_DELAY = 2  # 최소 대기 시간
MAX_DELAY = 8  # 최대 대기 시간

def random_delay():
    """랜덤한 시간만큼 대기 (봇 탐지 방지)"""
    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    print(f"  ⏳ {delay:.2f}초 대기 중... (봇 탐지 방지)")
    time.sleep(delay)

async def login_to_admin(page):
    """Admin 페이지에 로그인 (이미 로그인되어 있으면 건너뜀)"""
    print(f"🔐 Admin 페이지 확인: {ADMIN_URL}")
    
    try:
        await page.goto(ADMIN_URL, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(2)  # 페이지 로드 대기
        
        # 이미 로그인되어 있는지 확인
        current_url = page.url
        page_text = await page.inner_text('body')
        
        # 로그인 폼이 있는지 확인
        login_form = await page.query_selector('form')
        email_input = await page.query_selector('input[type="email"], input[name="email"]')
        password_input = await page.query_selector('input[type="password"]')
        
        # 로그인 폼이 없거나, admin 대시보드로 보이는 경우 이미 로그인된 것으로 판단
        if (not email_input and not password_input) or \
           ('dashboard' in page_text.lower() or 'projects' in page_text.lower() or 'admin' in current_url.lower()):
            print(f"  ✓ 이미 로그인되어 있습니다. 현재 URL: {current_url}")
            return True
        
        print(f"  🔐 로그인이 필요합니다. 로그인 진행...")
        
        # 디버깅: 페이지의 모든 input 필드 확인
        all_inputs = await page.query_selector_all('input')
        print(f"  🔍 발견된 input 필드 수: {len(all_inputs)}")
        for i, inp in enumerate(all_inputs):
            input_type = await inp.get_attribute('type')
            input_name = await inp.get_attribute('name')
            input_id = await inp.get_attribute('id')
            input_placeholder = await inp.get_attribute('placeholder')
            print(f"    Input {i+1}: type={input_type}, name={input_name}, id={input_id}, placeholder={input_placeholder}")
        
        random_delay()
        
        # 다양한 방법으로 이메일 입력 필드 찾기
        email_input = None
        email_selectors = [
            'input[type="email"]',
            'input[name="email"]',
            'input[id*="email" i]',
            'input[placeholder*="email" i]',
            'input[placeholder*="Email" i]',
            'input:not([type="password"]):not([type="submit"]):not([type="button"])'  # 첫 번째 텍스트 입력 필드
        ]
        
        for selector in email_selectors:
            try:
                email_input = await page.wait_for_selector(selector, timeout=3000)
                if email_input:
                    print(f"  ✓ 이메일 필드 발견: {selector}")
                    break
            except:
                continue
        
        if not email_input:
            # 페이지 HTML 저장하여 디버깅
            html_content = await page.content()
            debug_file = os.path.join(os.path.dirname(__file__), "admin_page_debug.html")
            with open(debug_file, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"  ⚠️  이메일 필드를 찾을 수 없습니다. 페이지 HTML을 {debug_file}에 저장했습니다.")
            return False
        
        await email_input.fill(ADMIN_EMAIL)
        print(f"  ✓ 이메일 입력 완료")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # 비밀번호 입력 필드 찾기
        password_input = None
        password_selectors = [
            'input[type="password"]',
            'input[name="password"]',
            'input[id*="password" i]',
            'input[placeholder*="password" i]',
            'input[placeholder*="Password" i]'
        ]
        
        for selector in password_selectors:
            try:
                password_input = await page.wait_for_selector(selector, timeout=3000)
                if password_input:
                    print(f"  ✓ 비밀번호 필드 발견: {selector}")
                    break
            except:
                continue
        
        if not password_input:
            print(f"  ❌ 비밀번호 필드를 찾을 수 없습니다.")
            return False
        
        await password_input.fill(ADMIN_PASSWORD)
        print(f"  ✓ 비밀번호 입력 완료")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # 로그인 버튼 찾기
        login_button = None
        button_selectors = [
            'button[type="submit"]',
            'input[type="submit"]',
            'button:has-text("Log in")',
            'button:has-text("Login")',
            'button:has-text("Sign in")',
            'button:has-text("로그인")',
            'form button',
            'form input[type="submit"]'
        ]
        
        for selector in button_selectors:
            try:
                login_button = await page.wait_for_selector(selector, timeout=3000)
                if login_button:
                    print(f"  ✓ 로그인 버튼 발견: {selector}")
                    break
            except:
                continue
        
        if not login_button:
            print(f"  ❌ 로그인 버튼을 찾을 수 없습니다.")
            return False
        
        await login_button.click()
        print(f"  ✓ 로그인 버튼 클릭")
        
        # 로그인 완료 대기
        await page.wait_for_load_state("networkidle", timeout=30000)
        await asyncio.sleep(3)  # 추가 대기
        
        # 로그인 성공 확인
        current_url = page.url
        print(f"  ✓ 로그인 후 현재 URL: {current_url}")
        
        # admin 페이지가 아닌 경우 로그인 성공으로 간주
        if 'admin' not in current_url.lower() or 'login' not in current_url.lower():
            print(f"  ✓ 로그인 성공으로 판단")
            return True
        else:
            # 페이지 내용 확인
            page_text = await page.inner_text('body')
            if 'dashboard' in page_text.lower() or 'projects' in page_text.lower():
                print(f"  ✓ 로그인 성공 (대시보드 확인)")
                return True
            else:
                print(f"  ⚠️  로그인 상태 불명확")
                return True  # 일단 진행
        
    except Exception as e:
        print(f"  ❌ 로그인 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

async def scrape_site_with_login(base_url, output_root_dir):
    """로그인 후 사이트 스크래이핑"""
    async with async_playwright() as p:
        # 브라우저를 headless=False로 실행하여 실제 브라우저처럼 보이게 함
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = await context.new_page()

        # Admin 페이지 로그인
        login_success = await login_to_admin(page)
        if not login_success:
            print("❌ 로그인에 실패했습니다. 스크래이핑을 중단합니다.")
            await browser.close()
            return

        # 로그인 후 메인 사이트로 이동
        print(f"\n📄 메인 사이트로 이동: {base_url}")
        await page.goto(base_url, wait_until="networkidle", timeout=60000)
        random_delay()

        visited_urls = set()
        to_visit_urls = {base_url}

        markdown_output_dir = os.path.join(output_root_dir, "markdown")
        images_output_dir = os.path.join(output_root_dir, "images")
        os.makedirs(markdown_output_dir, exist_ok=True)
        os.makedirs(images_output_dir, exist_ok=True)

        def get_project_name_from_url(url):
            parsed_url = urlparse(url)
            path_parts = [p for p in parsed_url.path.split('/') if p]
            if not path_parts or path_parts[-1].endswith(('.html', '.htm', '.php', '.asp')):
                project_name = path_parts[-1].replace('.html', '').replace('.htm', '') if path_parts else 'index'
                if not project_name:
                    project_name = 'index'
            else:
                project_name = os.path.basename(parsed_url.path)
            return project_name.replace(' ', '_').replace('/', '_')

        def get_markdown_path(url):
            parsed_url = urlparse(url)
            path_parts = [p for p in parsed_url.path.split('/') if p]
            if not path_parts or path_parts[-1].endswith(('.html', '.htm', '.php', '.asp')):
                filename = path_parts[-1].replace('.html', '').replace('.htm', '') if path_parts else 'index'
                if not filename:
                    filename = 'index'
                return os.path.join(markdown_output_dir, filename + '.md')
            else:
                return os.path.join(markdown_output_dir, os.path.basename(parsed_url.path) + '.md')

        page_count = 0
        while to_visit_urls:
            current_url = to_visit_urls.pop()
            if current_url in visited_urls:
                continue

            page_count += 1
            print(f"\n[{page_count}] 스크래이핑 중: {current_url}")
            visited_urls.add(current_url)

            try:
                await page.goto(current_url, wait_until="networkidle", timeout=60000)
                random_delay()  # 각 페이지 방문 후 랜덤 딜레이
                
                html_content = await page.content()
            except Exception as e:
                print(f"  ❌ 페이지 로드 실패: {e}")
                continue

            soup = BeautifulSoup(html_content, 'html.parser')
            current_page_project_name = get_project_name_from_url(current_url)

            # 이미지 다운로드
            img_count = 0
            for img_tag in soup.find_all('img', src=True):
                img_url = urljoin(current_url, img_tag['src'])
                parsed_img_url = urlparse(img_url)

                if parsed_img_url.netloc.endswith('cargo.site') and re.match(r'.*\.(jpg|jpeg|png|gif|svg|webp)$', img_url, re.IGNORECASE):
                    try:
                        project_images_sub_dir = os.path.join(images_output_dir, current_page_project_name)
                        os.makedirs(project_images_sub_dir, exist_ok=True)

                        image_filename = os.path.basename(parsed_img_url.path)
                        local_file_path = os.path.join(project_images_sub_dir, image_filename)
                        
                        # 이미지가 이미 다운로드되어 있으면 스킵
                        if os.path.exists(local_file_path):
                            print(f"  ⏭️  이미지 이미 존재: {image_filename}")
                            img_tag['src'] = os.path.relpath(local_file_path, markdown_output_dir)
                            continue
                        
                        # 이미지 다운로드
                        response = await page.request.get(img_url)
                        if response.ok:
                            with open(local_file_path, 'wb') as f:
                                f.write(await response.body())
                            img_count += 1
                            print(f"  📷 이미지 저장: {image_filename}")
                            await asyncio.sleep(random.uniform(0.3, 1.0))  # 이미지 다운로드 간 짧은 딜레이
                        else:
                            print(f"  ⚠️  이미지 다운로드 실패: {img_url} (상태: {response.status})")
                    except Exception as e:
                        print(f"  ❌ 이미지 저장 오류 {img_url}: {e}")

                    # img_tag src 업데이트
                    relative_image_path = os.path.relpath(local_file_path, markdown_output_dir)
                    img_tag['src'] = relative_image_path

            if img_count > 0:
                print(f"  ✓ {img_count}개 이미지 다운로드 완료")

            # 임베디드 동영상 링크 추출 (iframe, video 태그)
            video_links = []
            for iframe in soup.find_all('iframe'):
                src = iframe.get('src', '')
                if src:
                    video_links.append(src)
                    print(f"  🎥 임베디드 동영상 발견: {src}")
            
            for video in soup.find_all('video'):
                src = video.get('src', '')
                if src:
                    video_links.append(src)
                    print(f"  🎥 동영상 발견: {src}")

            # 마크다운 변환
            main_content_html = str(soup.body) if soup.body else html_content
            markdown_converter = html2text.HTML2Text()
            markdown_converter.ignore_links = False
            markdown_converter.ignore_images = False
            markdown_text = markdown_converter.handle(main_content_html)

            # 동영상 링크를 마크다운에 추가
            if video_links:
                markdown_text += "\n\n## 임베디드 동영상\n\n"
                for video_link in video_links:
                    markdown_text += f"- {video_link}\n"

            # 내부 링크 찾기
            for tag in soup.find_all(True, href=True):
                original_url = tag['href']
                absolute_url = urljoin(current_url, original_url)
                parsed_absolute_url = urlparse(absolute_url)

                if parsed_absolute_url.netloc == urlparse(base_url).netloc:
                    if absolute_url.endswith(('.html', '.htm', '.php', '.asp')) or not os.path.splitext(parsed_absolute_url.path)[1]:
                        if absolute_url not in visited_urls:
                            to_visit_urls.add(absolute_url)

            # 마크다운 파일 저장
            local_markdown_path = get_markdown_path(current_url)
            os.makedirs(os.path.dirname(local_markdown_path), exist_ok=True)
            with open(local_markdown_path, "w", encoding="utf-8") as f:
                f.write(markdown_text)
            print(f"  ✓ 마크다운 저장: {local_markdown_path}")

            # 다음 페이지로 가기 전 랜덤 딜레이
            if to_visit_urls:
                print(f"  📋 남은 페이지: {len(to_visit_urls)}개")
                random_delay()

        print(f"\n✅ 스크래이핑 완료!")
        print(f"   총 {page_count}개 페이지 처리")
        print(f"   출력 디렉토리: {output_root_dir}")

        await browser.close()

if __name__ == "__main__":
    base_url = "https://youjin.cargo.site/"
    output_directory = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective"
    
    print("=" * 60)
    print("CargoCollective Admin 스크래이핑 시작")
    print("=" * 60)
    print(f"대상 URL: {base_url}")
    print(f"출력 디렉토리: {output_directory}")
    print(f"랜덤 딜레이: {MIN_DELAY}~{MAX_DELAY}초")
    print("=" * 60)
    
    asyncio.run(scrape_site_with_login(base_url, output_directory))
