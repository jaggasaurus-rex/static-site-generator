from textnode import TextNode, TextType
from copystatic import source_to_destination, extract_title, generate_page

def main():
    source_to_destination()
    generate_page("content/index.md","template.html","public/index.html")

main()