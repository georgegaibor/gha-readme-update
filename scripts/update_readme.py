import os
import re

readme_path = 'README.md'

base_url = 'https://github.com/georgegaibor/gha-readme-update/tree/main/'

directory = '.'

# Get a list of part folders
part_folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder)) and folder.startswith('part')]

# Generate new part links
new_part_links = '\n'.join([f'- [x] [Part {folder[4:]}]({base_url}{folder})' for folder in sorted(part_folders)])

# Read the current README content
with open(readme_path, 'r') as file:
    content = file.read()

# Regular expression to find the part links section
part_links_section_pattern = re.compile(r'(- \[x\] \[Part \d+\]\(.*?\)\n?)+')

# Check if the part links section exists
if re.search(part_links_section_pattern, content):
    # Replace old part links section with new part links
    updated_content = re.sub(part_links_section_pattern, new_part_links + '\n', content)
else:
    # If no part links section is found, append the new part links at the end
    updated_content = content + '\n' + new_part_links

# Write the updated content back to the README file
with open(readme_path, 'w') as file:
    file.write(updated_content)
