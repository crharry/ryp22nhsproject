import json, htmlnode
links = []


    
file = open("../node/test.json","r").read()
#print(type(file))

#json to dict

jsonDict = json.loads(file)


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
                print(content["type"])
                print(type(content["content"]) , content["content"])
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

