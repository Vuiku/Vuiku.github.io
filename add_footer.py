import os
import re

def read_footer():
    """Read the footer content from footer.html"""
    with open('footer.html', 'r', encoding='utf-8') as f:
        return f.read()

def add_footer_to_html(html_file, footer_content):
    """Add footer to an HTML file before the closing body tag"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if footer is already present
    if '<!-- Footer Section -->' in content:
        print(f"Footer already exists in {html_file}")
        return
    
    # Add footer before closing body tag
    if '</body>' in content:
        new_content = content.replace('</body>', f'{footer_content}\n</body>')
    else:
        # If no body tag, add at the end
        new_content = content + '\n' + footer_content
    
    # Write the modified content back to file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Added footer to {html_file}")

def main():
    # Get the footer content
    try:
        footer_content = read_footer()
    except FileNotFoundError:
        print("Error: footer.html not found!")
        return
    
    # Find all HTML files in current directory and subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                add_footer_to_html(html_file, footer_content)

if __name__ == '__main__':
    main() 