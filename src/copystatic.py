import shutil
import os
from block_handler import markdown_to_html_node

def source_to_destination():
    source_path = "static"
    dest_path = "public"
    print("Deleting public directory...")
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    print("Copying statc files to public directory...")
    if os.path.exists(source_path):
        new_directory_generator(source_path,dest_path)

def new_directory_generator(source_path,dest_path):
    if os.path.isfile(source_path):
        print(f" * {source_path} -> {dest_path}")
        shutil.copy(source_path,dest_path)
    elif os.path.isdir(source_path):
        sub_source = os.listdir(source_path)
        for item in sub_source:
            new_source_path = os.path.join(source_path,item)
            new_dest_path = os.path.join(dest_path,item)
            if os.path.isdir(new_source_path):
                os.mkdir(new_dest_path)
            new_directory_generator(new_source_path,new_dest_path)

def extract_title(markdown):
    split = markdown.split("\n")
    title = ""
    for line in split:
        if line.startswith("# "):
            title = line[2:]
            break
    if title == "":
        raise Exception("No title line")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        article = f.read()
    title = extract_title(article)
    with open(template_path) as f:
        template = f.read()
    converted = markdown_to_html_node(article)
    content = converted.to_html()
    updated_title = template.replace("{{ Title }}", title)
    updated_content = updated_title.replace("{{ Content }}", content)
    file_dir = os.path.dirname(dest_path)
    os.makedirs(file_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(updated_content)
