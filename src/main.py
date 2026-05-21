from textnode import TextNode, TextType
import os
from copystatic import source_to_destination, extract_title, generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    source_to_destination()

    generate_page(dir_path_content,template_path,dir_path_public)

main()