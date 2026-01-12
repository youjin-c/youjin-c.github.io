#!/usr/bin/env python3
"""

import os
import re
import yaml
from pathlib import Path

def clean_markdown_content(content):
    """Clean the scraped markdown content by removing navigation elements and fixing links"""
    
    # Remove navigation elements and header links
    lines = content.split('\n')
    cleaned_lines = []
    skip_section = False
    for line in lines:
        # Skip lines that are part of the navigation
        if any(pattern in line for pattern in 
            [ ](https://cargo.site),
           [ ︎ ](/Left-Nav)',
   [ ]()',
            **[Youjin Chung](Home)**,
            [︎](https://www.linkedin.com/in/youjin-chung/),
            [︎](mailto:yjc433@nyu.edu),
       [︎](https://github.com/youjinChung),
            [#ML](https://youjin.io/ML),
            [#XR](https://youjin.io/XR),          [#Data](https://youjin.io/Data),  [#Interactive](https://youjin.io/Interactive)',
            [Archive](blog-1,            **[](Resume)**[](https://www.linkedin.com/in/youjin-chung/)'
        ]):
            continue
            
        # Skip empty lines at the beginning
        if not cleaned_lines and line.strip() == '':
            continue
            
        cleaned_lines.append(line)
    
    # Join lines back together
    content = '\n'.join(cleaned_lines)
    
    # Fix image paths to point to the images directory
    content = re.sub(r!\([^\]]*)\]\(([^)]+)\), r![\1({{ site.baseurl }}/images/\2)', content)
    
    # Fix internal links to other pages
    content = re.sub(r!\[([^\]]+)\]\(([^)]+\.md)\)', r[undefined1({{ site.baseurl }}/{% post_url \2 %})', content)
    
    # Remove any remaining cargo.site links
    content = re.sub(r'\[([^\]]*)\]\(https://[^)]+\)', r'\1', content)
    
    return content.strip()

def create_jekyll_post(markdown_file, output_dir):
    """Convert a markdown file to Jekyll post format"""
    # Read the markdown content
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the filename without extension
    filename = Path(markdown_file).stem
    
    # Clean the content
    cleaned_content = clean_markdown_content(content)
    
    # Create front matter
    front_matter = {
        'layout': 'post',
        'title': filename.replace('-', ' ').title(),
        'date': '2024-01-01',  # Default date, you can update this later
        'categories': ['portfolio'],
        'tags': []
    }
    
    # Add specific tags based on filename
    if 'ML' in filename or 'Machine-Learning' in filename:
        front_matter['tags'].append('machine-learning')
    if 'XR' in filename or 'VR' in filename or 'AR' in filename:
        front_matter['tags'].append('xr')
    if 'Data' in filename:
        front_matter['tags'].append('data')
    if 'Interactive' in filename or 'Game' in filename:
        front_matter['tags'].append('interactive')
    
    # Convert front matter to YAML
    yaml_content = yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)
    
    # Create the final Jekyll post content
    jekyll_post = f"""---
{yaml_content}---

{cleaned_content}
"""   
    # Write to output directory
    output_file = os.path.join(output_dir, f"{filename}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(jekyll_post)
    
    print(f"Created Jekyll post: {output_file}")

def main():
    # Paths
    scraped_dir = "portfolio-site/youjin.cargo.site_scraped/markdown"
    output_dir = "_posts"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all markdown files from scraped directory
    markdown_files = []
    for file in os.listdir(scraped_dir):
        if file.endswith('.md') and file != 'stylesheet.md' and file != 'rss.md':
            markdown_files.append(os.path.join(scraped_dir, file))
    
    # Convert each file
    for markdown_file in markdown_files:
        create_jekyll_post(markdown_file, output_dir)
    
    print(f"Converted {len(markdown_files)} files to Jekyll posts")

if __name__ == "__main__":
    main() 