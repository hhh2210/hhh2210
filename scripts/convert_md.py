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
    
    generated_posts = [] # 用于存储博文信息 (标题, HTML文件名)

    if not md_files:
        print(f"No Markdown files found in {abs_blog_dir}.")
        # 即使没有找到md文件，也尝试创建空的index.html
    else:
        # 排除可能的 index.md，避免自我处理，也排除其他不希望作为单独博文处理的md文件
        md_files_to_process = [
            mf for mf in md_files if not os.path.basename(mf).lower().startswith('index.')
        ]

        for md_file_path in md_files_to_process:
            print(f"Processing: {md_file_path}")
            
            # Calculate depth for HTML scaffold's relative paths
            # This is the number of directory levels from the workspace root to the HTML file's directory
            # e.g. for "blog/post.md", its dir is "blog", relative to root "blog", depth = 1
            # e.g. for "blog/category/post.md", its dir is "blog/category", relative to root "blog/category", depth = 2
            html_dir_relative_to_root = os.path.relpath(os.path.dirname(md_file_path), workspace_root)
            depth = len(os.path.normpath(html_dir_relative_to_root).split(os.sep))
            if html_dir_relative_to_root == '.': # Should not happen if blog_dir_from_root is specified
                depth = 0


            base_name_os = os.path.splitext(md_file_path)[0] # 使用 os.path.splitext
            html_file_path = base_name_os + ".html"
            # HTML文件名相对于 blog 目录，用于在 blog/index.html 中生成链接
            html_file_name_relative_to_blog_dir = os.path.relpath(html_file_path, abs_blog_dir)


            with open(md_file_path, 'r', encoding='utf-8') as f_md:
                md_content = f_md.read()

            title = os.path.basename(base_name_os).replace('-', ' ').replace('_', ' ').title() 
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
            generated_posts.append((title, html_file_name_relative_to_blog_dir))

    # --- 生成 blog/index.html ---
    index_md_content_list = ["# 博客文章列表\\n"] # Markdown H1 for the list page title
    if not generated_posts:
        index_md_content_list.append("\\n暂无文章。")
    else:
        # 按标题排序文章列表 (或者可以按文件名或其他方式排序)
        for post_title, post_html_filename in sorted(generated_posts): 
            index_md_content_list.append(f"- [{post_title}]({post_html_filename})") # Markdown list item
    
    index_md_content_final = "\\n".join(index_md_content_list)
    
    # blog/index.html 的深度计算
    # abs_blog_dir 是 blog 目录的绝对路径
    # html_dir_relative_to_root for index.html (in blog dir) is 'blog' if blog_dir_from_root is 'blog'
    index_page_dir_relative_to_root = os.path.relpath(abs_blog_dir, workspace_root)
    index_depth = len(os.path.normpath(index_page_dir_relative_to_root).split(os.sep))
    # 如果 blog_dir_from_root 指向的是 workspace_root (例如，脚本参数是 ".")
    # 那么 index_page_dir_relative_to_root 会是 "."，此时深度应为 0
    if index_page_dir_relative_to_root == '.': 
        index_depth = 0
    
    # 使用 'nl2br' 和 'sane_lists' 扩展来渲染列表
    index_html_fragment = markdown.markdown(index_md_content_final, extensions=['nl2br', 'sane_lists'])
    
    # 注意：index.html 的页面 <title> 和 <h1> 将是 "博客列表"
    full_index_html_content = create_html_scaffold("博客列表", index_html_fragment, blog_path_depth=index_depth)
    
    final_index_html_path = os.path.join(abs_blog_dir, "index.html")
    with open(final_index_html_path, 'w', encoding='utf-8') as f_index_html:
        f_index_html.write(full_index_html_content)
    print(f"Generated blog index: {final_index_html_path}")

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