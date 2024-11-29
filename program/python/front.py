import json
from htmlnode import *  


    
file = open("../node/test.json","r").read()
#print(type(file))


#json to dict
jsonDict = json.loads(file)
#print(jsonDict)



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
            ##used to be its own def
            if content["type"] == "img":
                htmlArray.append(htmlImageObject(url= content["attributes"]["src"]))
            elif content["type"] == "a":
                if "attributes" in content:
                    if "href" in content["attributes"]:
                        htmlArray.append(htmlAObject(url= content["attributes"]["href"],text= content["content"][0]))##'text' to be recursive allowing for images
                    else:
                        print("improper Link")
                else:
                    print("improper Link")

            elif "content" in content: ###no images and anchors should reach here
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
    
    



