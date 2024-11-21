class htmlObject:
    text = ""
    def __init__(self,text):
        self.text = text
    def __str__(self):
        return self.text


class htmlImageObject(htmlObject):
    url = ""
    def __init__(self,alttext = "imgAltText",url = "www.example.com"):
            super().__init__(alttext)
            self.url = url



class htmlAObject(htmlObject):
    url = ""
    def __init__(self,text = "linkText",url = "www.example.com"):
        def __init__(self,alttext = "imgAltText",url = "www.example.com"):
            super().__init__(text)
            self.url = url