import os
import re

def fix_links(content):
    # Replace GitHub-style links with Hugo-style links
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'[[\1]]({{\< ref "\2" >}})', content)
    
    # Replace image links
    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'{{< figure src="\2" alt="\1" >}}', content)
    
    return content

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    updated_content = fix_links(content)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)
                print(f"Processed: {file_path}")

# Usage
content_directory = 'content/posts/daily-glider'
process_directory(content_directory)
