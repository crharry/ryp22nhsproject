import json
from htmlnode import *  
links = []


    
file = open("../node/test.json","r").read()
#print(type(file))

#json to dict

jsonDict = json.loads(file)
print(jsonDict)

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


#ignored assumed html tag
#loop through "root" tags (head, body, foot, etc)
i = 0
for x in jsonDict["content"]:
    #print("for loop: " , i)
    i = i + 1
    #print(x)
    recurisvePrinter(x)


##note
##add strings as htmlobject."text", 
##add objects as (htmlobject) children



def htmlnodeifier(jsonDict):
    print('creating object################')
    print("jsondict: ", jsonDict)
    #print(type(jsonDict))



    elementname = jsonDict["type"]
    newchild = htmlObject(elementname,True,True,'text',None)
    print(newchild.elementname)
    #print(jsonDict["content"]) 
    #print(type(jsonDict["content"]))
    #print(type(jsonDict["content"][0]))
    if "content" in jsonDict:
        if (type(jsonDict["content"][0]) == str) and (len(jsonDict["content"]) > 0):
            print("there is a string here " + jsonDict["content"][0])
            newchild.text = jsonDict["content"][0]

            if (len(jsonDict["content"]) > 1):
                jsonDict["content"] = jsonDict["content"][1:]
                for x in jsonDict["content"]:
                    #print(x)
                    #print(type(x))
                    if (type(x) == ""):
                        print("breaking because of string or none")
                    else:
                        newNewChild = htmlnodeifier(x)
                        print (newNewChild)
                        newchild.addChild(newNewChild)

            return newchild
            ####add elif for dealing with objects with string and object contents
        else:
            for x in jsonDict["content"]:
                #print(x)
                #print(type(x))
                if (type(x) == ""):
                    print("breaking because of string or none")
                else:
                    newNewChild = htmlnodeifier(x)
                    print (newNewChild)
                    newchild.addChild(newNewChild)
    
    ##__init__(self,elementname,isVisible,inline,text,children)
    #if child(ren) has child(ren):
    #    htmlnodeifier(children)



htmlnodeifier(jsonDict)