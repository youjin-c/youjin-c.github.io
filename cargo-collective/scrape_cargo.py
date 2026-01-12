import asyncio
import os
from playwright.async_api import async_playwright

async def scrape_page(url, output_dir):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        
        # Wait for the page to be fully loaded, including dynamic content
        await page.wait_for_load_state('networkidle')

        # Get the full HTML content
        html_content = await page.content()

        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Save the HTML content
        file_path = os.path.join(output_dir, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Saved {url} to {file_path}")

        await browser.close()

if __name__ == "__main__":
    base_url = "https://youjin.cargo.site/"
    output_directory = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective" # New directory for scraped content
    asyncio.run(scrape_page(base_url, output_directory))
