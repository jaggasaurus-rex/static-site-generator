from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from rawmarkdown import split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
from block_handler import markdown_to_blocks, block_to_block_type, markdown_to_html_node

def easytestcase():
    md = """
This is **bolded** paragraph
text in a p

> fuck bitches

# tag here

## fucking head 2 bitch

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)

def easytestcase2():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)

def easytestcase3():
    md = """
This is **bolded** paragraph
text in a p

> fuck bitches

> get hoes
> is what
> I've been saying

- this is
- a fucking
- list bitch

1. this is
2. an ordered
3. list bitch

# tag here

## another tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)

easytestcase2()