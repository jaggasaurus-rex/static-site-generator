from enum import Enum

from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node, TextNode, TextType
from rawmarkdown import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    final = []
    for block in blocks:
        if block == "":
            continue
        final.append(block.strip())
    return final

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    if block.startswith("1. "):
        og = 0
        for line in lines:
            og += 1
            if not line.startswith(f"{og}. "):
                return BlockType.PARAGRAPH
        return BlockType.OLIST
    return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    outter_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            inner_text = block[4:-3]
            code_leaf = LeafNode("code", inner_text)
            pre_parent = ParentNode("pre",[code_leaf])
            outter_parent = pre_parent
        else:
            outter_parent = type_to_tag(block, block_type)
        outter_children.append(outter_parent)


    final_node = ParentNode("div", outter_children)
    return final_node


def type_to_tag(text, type):
    if type == BlockType.PARAGRAPH:
        text_value = paragraph_to_html(text)
        text_node = text_to_textnodes(text_value)
        children = text_to_children(text_node)
        outter_parent = ParentNode("p", children)
        return outter_parent
    if type == BlockType.QUOTE:
        split_text = text.split("\n")
        text_value = ""
        for item in split_text:
            text_value += f"{item[2:]} "
        text_value = text_value.strip()
        text_node = text_to_textnodes(text_value)
        children = text_to_children(text_node)
        outter_parent = ParentNode("blockquote", children)
        return outter_parent
    if type == BlockType.ULIST:
        children = ulist_to_html(text)
        outter_parent = ParentNode("ul", children)
        return outter_parent
    if type == BlockType.OLIST:
        children = olist_to_html(text)
        outter_parent = ParentNode("ol", children)
        return outter_parent
    if type == BlockType.HEADING:
        tag, text_value = heading_to_html(text)
        text_node = text_to_textnodes(text_value)
        children = text_to_children(text_node)
        outter_parent = ParentNode(tag, children)
        return outter_parent
    raise ValueError("Error: Not a valid block type")
    
def heading_to_html(text):
    if text.startswith("# "):
        level = 1
    elif text.startswith("## "):
        level = 2
    elif text.startswith("### "):
        level = 3
    elif text.startswith("#### "):
        level = 4
    elif text.startswith("##### "):
        level = 5
    elif text.startswith("###### "):
        level = 6
    else:
        raise ValueError("Error: Not a valid block type")
    tag = f"h{level}"
    value = text[level + 1:]
    return tag, value

def paragraph_to_html(text):
    new_text = text.replace("\n", " ")
    return new_text

def ulist_to_html(text):
    ulist_items = text.split("\n")
    full = []
    for item in ulist_items:
        text_node = text_to_textnodes(item[2:])
        children = text_to_children(text_node)
        outter_parent = ParentNode("li", children)
        full.append(outter_parent)
    return full

def olist_to_html(text):
    olist_items = text.split("\n")
    full = []
    for item in olist_items:
        inner = item.split(". ", 1)[1]
        text_node = text_to_textnodes(inner)
        children = text_to_children(text_node)
        outter_parent = ParentNode("li", children)
        full.append(outter_parent)
    return full

def text_to_children(text):
    children = []
    for node in text:
        leaf_node = text_node_to_html_node(node)
        children.append(leaf_node)
    return children