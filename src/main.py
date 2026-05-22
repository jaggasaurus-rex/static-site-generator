from textnode import TextNode, TextType
import os
from copystatic import source_to_destination, extract_title, generate_page
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"

    print(base_path)
    source_to_destination()

    generate_page(dir_path_content,template_path,dir_path_public, base_path)

main()