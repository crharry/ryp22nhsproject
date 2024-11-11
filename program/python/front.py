import json
links = []


    
file = open("../node/test.json","r").read()
#print(type(file))

#json to dict
jsonDict = json.loads(file)

#print(jsonDict)
#print(jsonDict["type"])
#print(type(jsonDict["content"]))
#print(type(jsonDict))
#print(len(jsonDict))

#print(jsonDict["type"])
#print(jsonDict["content"])
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
            #print(content["type"])
            #print(type(content["content"]) , content["content"])
            if type(content["content"]) == type([]) :
                for y in content["content"]:
                    recurisvePrinter(y)
            else:
                return

        


#ignored assumed html tag
#loop through "root" tags (head, body, foot, etc)
for x in jsonDict["content"]:
    #print("for loop: " , x)
    recurisvePrinter(x)

