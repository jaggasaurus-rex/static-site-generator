from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from rawmarkdown import split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
from block_handler import markdown_to_blocks, block_to_block_type

def easytestcase():
    md = """
#### This is **bolded** paragraph



''' this is code'''

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


>This is another paragraph with _italic_ text and `code` here
>This is the same paragraph on a new line

- This is a list
- with items

1. This is a list
2. with items
3. and more
4. items
"""
    blocks = markdown_to_blocks(md)
    blocktype = block_to_block_type(blocks[0])
    print(blocktype)

easytestcase()