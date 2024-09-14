import os
import re

# Dictionary mapping folder names to desired titles
title_map = {
    "get-started": "Get Started",
    "limit-and-offset": "Limit and Offset",
    "arbitrary-logic": "Arbitrary Logic",
    "boosting-declarative-part": "Boosting the declarative part",
    "debug-technique": "Debug Technique",
    "functions": "Functions",
    "instructions": "Instructions",
    "contracts": "Contracts",
    "setup-and-style": "Setup and Writing Style",
    "contract": "Contract",
    "function": "Function",
    "instruction": "Instruction",
    "low-level-data-1": "Low-Level Data (part 1)",
    "low-level-data-2": "Low-Level Data (part 2)",
    "handy-scripts": "Handy Scripts and SQL Queries"
}

def update_front_matter(file_path, new_title):
    with open(file_path, 'r') as file:
        content = file.read()

    # Check if front matter exists
    front_matter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    
    if front_matter_match:
        # Update existing front matter
        front_matter = front_matter_match.group(1)
        updated_front_matter = re.sub(r'title: .*', f'title: "{new_title}"', front_matter)
        content = re.sub(r'^---\s*\n.*?\n---\s*\n', f'---\n{updated_front_matter}\n---\n', content, flags=re.DOTALL)
    else:
        # Add new front matter
        content = f'---\ntitle: "{new_title}"\n---\n\n{content}'

    with open(file_path, 'w') as file:
        file.write(content)

def process_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'index.md' in filenames:
            folder_name = os.path.basename(dirpath)
            if folder_name in title_map:
                file_path = os.path.join(dirpath, 'index.md')
                update_front_matter(file_path, title_map[folder_name])
                print(f"Updated {file_path}")

# Usage
root_directory = 'content/posts/daily-glider'
process_directories(root_directory)