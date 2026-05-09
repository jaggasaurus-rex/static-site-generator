class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        html_list = ""
        if self.props is None:
            return ""
        for i in self.props:
            value = self.props[i]
            html_list+= f' {i}="{value}"'
        return html_list

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, props={self.props})'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid Parent: no tag")
        if self.children is None:
            return ValueError("invaled HTML: Children No Value")
        
        full_string = ""

        for child in self.children:
            full_string += child.to_html()
        

        return f"<{self.tag}{self.props_to_html()}>{full_string}</{self.tag}>"

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, children={self.children}, props={self.props})'