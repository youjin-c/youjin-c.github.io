import asyncio
import os
import re
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import html2text

async def scrape_site(base_url, output_root_dir):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

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

        # Removed handle_route function
        # await page.route(re.compile(r".*"), handle_route) # This line is also removed

        while to_visit_urls:
            current_url = to_visit_urls.pop()
            if current_url in visited_urls:
                continue

            print(f"Scraping: {current_url}")
            visited_urls.add(current_url)

            try:
                await page.goto(current_url, wait_until="domcontentloaded", timeout=60000)
                html_content = await page.content()
            except Exception as e:
                print(f"Error navigating to {current_url}: {e}")
                continue

            soup = BeautifulSoup(html_content, 'html.parser')
            current_page_project_name = get_project_name_from_url(current_url)

            for img_tag in soup.find_all('img', src=True):
                img_url = urljoin(current_url, img_tag['src'])
                parsed_img_url = urlparse(img_url)

                if parsed_img_url.netloc.endswith('cargo.site') and re.match(r'.*\.(jpg|jpeg|png|gif|svg|webp)$', img_url, re.IGNORECASE):
                    try:
                        project_images_sub_dir = os.path.join(images_output_dir, current_page_project_name)
                        os.makedirs(project_images_sub_dir, exist_ok=True)

                        image_filename = os.path.basename(parsed_img_url.path)
                        local_file_path = os.path.join(project_images_sub_dir, image_filename)
                        
                        # Download image directly using page.request
                        response = await page.request.get(img_url)
                        if response.ok:
                            with open(local_file_path, 'wb') as f:
                                f.write(await response.body())
                            print(f"Saved image: {img_url} to {local_file_path}")
                        else:
                            print(f"Failed to download image {img_url}: {response.status}")
                    except Exception as e:
                        print(f"Error saving image {img_url}: {e}")

                    # Update img_tag src to point to the new local path
                    relative_image_path = os.path.relpath(local_file_path, markdown_output_dir)
                    img_tag['src'] = relative_image_path

            main_content_html = str(soup.body) if soup.body else html_content
            markdown_converter = html2text.HTML2Text()
            markdown_converter.ignore_links = False
            markdown_converter.ignore_images = False
            markdown_text = markdown_converter.handle(main_content_html)

            for tag in soup.find_all(True, href=True):
                original_url = tag['href']
                absolute_url = urljoin(current_url, original_url)
                parsed_absolute_url = urlparse(absolute_url)

                if parsed_absolute_url.netloc == urlparse(base_url).netloc:
                    if absolute_url.endswith(('.html', '.htm', '.php', '.asp')) or not os.path.splitext(parsed_absolute_url.path)[1]:
                        to_visit_urls.add(absolute_url)

            local_markdown_path = get_markdown_path(current_url)
            os.makedirs(os.path.dirname(local_markdown_path), exist_ok=True)
            with open(local_markdown_path, "w", encoding="utf-8") as f:
                f.write(markdown_text)
            print(f"Saved markdown for {current_url} to {local_markdown_path}")

        await browser.close()

if __name__ == "__main__":
    base_url = "https://youjin.cargo.site/"
    output_directory = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective"
    asyncio.run(scrape_site(base_url, output_directory))