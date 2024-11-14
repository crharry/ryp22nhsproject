class htmlObject:
    elementname = ""
    isVisible = True
    inline = False
    text = ""
    children = []
    def __init__(self,elementname,isVisible,inline,text,children):
        self.elementname = elementname
        self.isVisible = isVisible
        self.inline = inline
        self.text = text
        children = children
    def addChild(newchild):
        children.append(newchild)
    


class htmlImageObject:
    url = ""
    def __init__(self,elementname = "img",isVisible = True,inline = True,alttext = "imgAltText",url = "www.example.com"):
            super().__init__(self,elementname,isVisible,inline,alttext,None)
            self.url = url
            ##(self,isVisible,inline,children = Null)



class htmlAObject:
    url = ""
    def __init__(self,elementname = "a",isVisible = True,inline = True,text = "linkText",url = "www.example.com",children=[]):
            super().__init__(self,elementname,isVisible,inline,alttext,children)
            self.url = url