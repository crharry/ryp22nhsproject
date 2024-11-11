class htmlObject:
    bool isVisible = True
    bool inline = False
    str text
    children = []
    def __init__(self,isVisible,inline,text,children):
        self.isVisible = isVisible
        self.inline = inline
        children = children
    def addChild(newchild):
        children.append(newchild)
    


class htmlImageObject:
    str url
    def __init__(self,isVisible,inline,alttext,children):
            super().__init__(self,isVisible,inline,children):



class htmlAObject:
    str url
    def __init__(self,isVisible,inline,text,children):
            super().__init__(self,isVisible,inline,children):