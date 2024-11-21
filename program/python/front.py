import json
from htmlnode import *  
links = []


    
file = open("../node/test.json","r").read()
#print(type(file))

#json to dict

jsonDict = json.loads(file)
#print(jsonDict)

##arrays for styling(?)

#recursive loop for json
def recurisvePrinter(content):
    #content = content[0]
    #print(type(content) , content)

    if type(content) == type("") :
        print(content)
        return
    else:
        if type(content) == type(dict()):
            if "content" in content:
                #print(content["type"])
                #print(type(content["content"]) , content["content"])
                if type(content["content"]) == type([]) :
                    for y in content["content"]:
                        recurisvePrinter(y)
                else:
                    return

        else:
            return


def arrayifierLinkAndImageDealer(element):

    if element["type"] == "img":
        
        htmlArray.append(htmlImageObject(url= element["attributes"]["src"]))
    if element["type"] == "a":
        if "attributes" in element:
            if "href" in element["attributes"]:
                htmlArray.append(htmlAObject(url= element["attributes"]["href"]))
            else:
                print("improper Link")
        else:
            print("improper Link")

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
            if "content" in content:
                #print(content["type"])
                #print(type(content["content"]) , content["content"])
                if type(content["content"]) == type([]) :
                    for y in content["content"]:
                        arrayifier(y)
                else:
                    return
        else:
            return


for x in jsonDict["content"]:
    #print(x)
    arrayifier(x)


#ignored assumed html tag
#loop through "root" tags (head, body, foot, etc)

x = 0
while x < len(htmlArray):
    print(htmlArray[x],end = "")
    input("")
    x = x + 1



