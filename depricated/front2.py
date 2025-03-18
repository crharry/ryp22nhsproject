import json
from htmlnode import *  
import urwid
import searcher
import time
 


#json to dict
jsonDict = ""
print(jsonDict)


##button used for links
class BoxButton(urwid.WidgetWrap):
    """ Taken from https://stackoverflow.com/a/65871001/778272
    """
    def __init__(self, label,URL):
        self.URL = URL
        self.widget = urwid.LineBox(label)
        self.hidden_button = urwid.Button('hidden button',lambda a : openLink(URL))
        super(BoxButton, self).__init__(self.widget)

    def selectable(self):
        return True

    def mouse_event(self, *args, **kwargs):
        return self.hidden_button.mouse_event(*args, **kwargs)
    
    
def linkButton(button):
    print(button.URL)
    openLink(URL)
def openLink(url):
    print(url)
    time.sleep(5) 
    searcher.search(url)
    time.sleep(5) 
    file = open("../node/test.json","r").read()
    #print(type(file))    
    #json to dict
    jsonDict = json.loads(file)

    display(jsonDict)




##recursive json to urwid
def urwider(json):
    if type(json) == type(""): ## text leaf node
        print(json)
        return [urwid.Text(json)]
    if type(json) == type([]):
        if type(json[0]) == urwid.Text("None"):
            print("urwidobj")
    elif type(json) == type(dict()):##JS Object (anything but plain text)
        if json["type"].lower() == "a":
                if "attributes"  in json:
                    if ("HREF" in json["attributes"]):
                        json["attributes"]["href"] = json["attributes"]["HREF"]
                    if ("href" in json["attributes"]):
                        ##deal with link
                        ##get link text
                        links = []
                        buttonLinks = []
                        url = json["attributes"]["href"]
                        for y in json["content"]:
                            links = links + urwider(y)
                        for y in links:
                            buttonLinks.append(BoxButton(y,url))
                            
                        return buttonLinks
                        ##replace urwid.text with buttons containing text
                        ##get link url
                        ##make button(label,on_press,user_data,align,wrap,layout)
                        
                        
                    else:
                        print("improper Link")
                        return [urwid.Text("improper Link")]
                else:
                    print("improper Link")
                    return [urwid.Text("improper Link")]

        ##for each child, urwider(child)
        elif "content" in json:#has child(ren)
            temparray = []
            if type(json["content"]) == type([]):##has multiple children                    
                for y in json["content"]:
                    temparray = temparray + urwider(y)
            else:
                temparray = [urwider(json["content"])]
            ##add each child to area
            return [urwid.Pile(temparray)]
        else:
            return [urwid.Text("None")]
        ##create new area
    ##return array of areas

def display(jsonDict):
    print(jsonDict)
    urwidUI = urwid.ScrollBar(urwid.Scrollable(urwid.Filler(urwider(jsonDict)[0])))
    loop = urwid.MainLoop(urwidUI)
    loop.screen.clear()
    loop.run()

