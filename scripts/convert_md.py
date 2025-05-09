import markdown
import os
import glob
import sys

def create_html_scaffold(title, content_html, blog_path_depth=1):
    """
    Generates the full HTML page structure for a blog post.
    blog_path_depth indicates how deep the blog post is from the root 
    (where style.css is located) to correctly link CSS and navigation.
    For style.css at root:
    - blog/post.html needs depth 1 (../style.css)
    - blog/category/post.html needs depth 2 (../../style.css)
    """
    relative_path_prefix = "../" * blog_path_depth
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="{relative_path_prefix}style.css">
</head>
<body>
    <header>
        <nav>
            <a href="{relative_path_prefix}">首页</a>
            <a href="{relative_path_prefix}blog/">博客</a>
        </nav>
        <h1>{title}</h1> 
    </header>
    <main>
        <article>
{content_html}
        </article>
    </main>
    <footer>
        <p>&copy; 2024 您的名字</p>
    </footer>
</body>
</html>"""

def convert_directory(blog_dir_from_root="blog"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.dirname(script_dir) # Assumes script is in <root>/scripts/
    
    # Absolute path to the blog directory
    abs_blog_dir = os.path.join(workspace_root, blog_dir_from_root)
    print(f"Looking for Markdown files in: {abs_blog_dir}")

    md_files = glob.glob(os.path.join(abs_blog_dir, "**/*.md"), recursive=True)
    
    if not md_files:
        print(f"No Markdown files found in {abs_blog_dir}.")
        return

    for md_file_path in md_files:
        print(f"Processing: {md_file_path}")
        
        # Calculate depth for HTML scaffold's relative paths
        # This is the number of directory levels from the workspace root to the HTML file's directory
        # e.g. for "blog/post.md", its dir is "blog", relative to root "blog", depth = 1
        # e.g. for "blog/category/post.md", its dir is "blog/category", relative to root "blog/category", depth = 2
        html_dir_relative_to_root = os.path.relpath(os.path.dirname(md_file_path), workspace_root)
        depth = len(os.path.normpath(html_dir_relative_to_root).split(os.sep))
        if html_dir_relative_to_root == '.': # Should not happen if blog_dir_from_root is specified
            depth = 0


        base_name = os.path.splitext(md_file_path)[0]
        html_file_path = base_name + ".html"

        with open(md_file_path, 'r', encoding='utf-8') as f_md:
            md_content = f_md.read()

        title = os.path.basename(base_name).replace('-', ' ').replace('_', ' ').title() 
        lines = md_content.split('\n', 1) 
        if lines and lines[0].startswith('# '):
            title = lines[0][2:].strip()
        
        html_fragment = markdown.markdown(md_content, extensions=[
            'fenced_code', 
            'codehilite', 
            'tables', 
            'toc',
            'sane_lists',
            'nl2br' # Convert newlines to <br>
        ])
        
        full_html_content = create_html_scaffold(title, html_fragment, blog_path_depth=depth)

        with open(html_file_path, 'w', encoding='utf-8') as f_html:
            f_html.write(full_html_content)
        print(f"Converted: {md_file_path} -> {html_file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {os.path.basename(__file__)} <blog_directory_relative_to_root>")
        print(f"Example: python {os.path.basename(__file__)} blog")
        sys.exit(1)
        
    blog_directory_arg = sys.argv[1]
    
    # Security check: ensure blog_directory_arg is a simple relative path (no '..')
    if ".." in blog_directory_arg.split(os.sep):
        print(f"Error: Invalid blog directory path '{blog_directory_arg}'. Must be a relative path from the workspace root without '..'.")
        sys.exit(1)

    # Assuming the script is run from the workspace root in GitHub Actions
    # So, blog_directory_arg is directly the path from root, e.g., "blog"
    convert_directory(blog_directory_arg) 