from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from rawmarkdown import split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
from block_handler import markdown_to_blocks, block_to_block_type, markdown_to_html_node
import os

def easytestcase():
    name, ext = os.path.splitext("index.md")
    print(f"Name: {name}\nExt: {ext}")

easytestcase()