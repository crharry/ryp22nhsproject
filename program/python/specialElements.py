import urwid,time,requests
import typing

##button used for links
class BoxButton(urwid.WidgetWrap):
    """ Taken from https://stackoverflow.com/a/65871001/778272
    """
    def __init__(self, label,URL):
        self.URL = URL
        self.widget = urwid.LineBox(label)
        self.hidden_button = urwid.Button('hidden button')
        super(BoxButton, self).__init__(self.widget)

    def selectable(self):
        return True

    def mouse_event(self, *args, **kwargs):
        print(self.URL)
        request = requests.get(self.URL)
        print(request.text)
        return request.text



class a():
    ##a element

    url = ""
    children = []##other widgets
    canHaveChildren = True
    hasListener = True
    pile = None
    def __init__(self,url,children=[]):
        self.url = url
        self.children = children

    def pileChildren(self):
        self.children.append(urwid.Button(self.url))
        self.pile = urwid.LineBox(urwid.Pile((self.children)))
    def setUrl(self,url):
        self.url = url
    def get(self):
        return self.pile,self.children[-1]

