from textnode import TextNode, TextType

print("hello world")



def main():
    test_object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(f"TextNode({test_object})")


main()