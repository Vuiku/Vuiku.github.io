import os
import re
import argparse

def read_footer():
    """Read the footer content from footer.html"""
    try:
        with open('footer.html', 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Error: footer.html not found!")
        return None

def remove_footer_from_file(file_path):
    if file_path == 'footer.html':
        print("Footer.html is not allowed to be removed")
        return False
    else:
        
        """Remove footer section from an HTML file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the entire footer section including comments
        footer_pattern = r'<!--\s*Footer Section\s*-->[\s\S]*?</footer>'
        
        # Check if footer exists
        if re.search(footer_pattern, content):
            # Remove the footer
            new_content = re.sub(footer_pattern, '', content)
            
            # Write the modified content back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Footer removed from {file_path}")
            return True
        else:
            print(f"No footer found in {file_path}")
            return False

def add_footer_to_file(file_path, footer_content):
    """Add footer to an HTML file before the closing body tag"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if footer already exists
    if '<!-- Footer Section -->' in content:
        print(f"Footer already exists in {file_path}")
        return False
    
    # Add footer before closing body tag
    if '</body>' in content:
        new_content = content.replace('</body>', f'{footer_content}\n</body>')
    else:
        # If no body tag, add at the end
        new_content = content + '\n' + footer_content
    
    # Write the modified content back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Footer added to {file_path}")
    return True

def process_files(action='add'):
    """Process all HTML files in the project"""
    if action not in ['add', 'remove', 'update']:
        print(f"Invalid action: {action}")
        return
    
    if action in ['add', 'update']:
        footer_content = read_footer()
        if not footer_content:
            return
    
    # Walk through all directories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html') and file != 'footer.html':
                file_path = os.path.join(root, file)
                
                if action == 'remove':
                    remove_footer_from_file(file_path)
                elif action == 'add':
                    add_footer_to_file(file_path, footer_content)
                elif action == 'update':
                    remove_footer_from_file(file_path)
                    add_footer_to_file(file_path, footer_content)

def main():
    parser = argparse.ArgumentParser(description='Manage footer in HTML files')
    parser.add_argument('action', choices=['add', 'remove', 'update'],
                      help='Action to perform: add, remove, or update footer')
    
    args = parser.parse_args()
    
    print(f"Starting footer {args.action} process...")
    process_files(args.action)
    print(f"Footer {args.action} completed!")

if __name__ == '__main__':
    main() 