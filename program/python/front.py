import json
from htmlnode import *  


    
file = open("../node/test.json","r").read()
#print(type(file))


#json to dict
jsonDict = json.loads(file)
#print(jsonDict)

def arrayifierLinkAndImageDealer(element):

    if element["type"] == "img":
        
        htmlArray.append(htmlImageObject(url= element["attributes"]["src"]))
    if element["type"] == "a":
        if "attributes" in element:
            if "href" in element["attributes"]:
                htmlArray.append(htmlAObject(url= element["attributes"]["href"],text= element["content"][0]))##'text' to be recursive allowing for images
            else:
                print("improper Link")
        else:
            print("improper Link")


def anchorTagObjectifier(anchor):
    htmlAObject(url= element["attributes"]["href"],text= element["content"][0])
    ##for each content make new AObject
    ##just text
    ##just image
    ##text and image
    ##some other tag(s)

    ##for each child
    ##arrayifierLinkAndImageDealer(childhref)


htmlArray = []
def arrayifier(content):

    if type(content) == type("") :
        htmlArray.append(content)
        return
    else:
        if type(content) == type(dict()):
            ##add if for forms
            if (content["type"] == "img") or (content["type"] == "a"):
                arrayifierLinkAndImageDealer(content)
            elif "content" in content:
                #print(content["type"])
                #print(type(content["content"]) , content["content"])
                if type(content["content"]) == type([]) :
                    for y in content["content"]:
                        arrayifier(y)
                else:
                    return
        else:
            return

#ignored assumed html tag
#loop through "1st child" tags (head, body, foot, etc)
for x in jsonDict["content"]:
    #print(x)
    arrayifier(x)




x = 0
print(len(htmlArray))
print(htmlArray)
while x < len(htmlArray):
    inputval = input(htmlArray[x])
    if inputval == "":
        x = x + 1
    
    



