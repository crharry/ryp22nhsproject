import urwid
import searcher
import re


file = open("../node/index.html","r").read()
#print(file)



# Removing HTML <script> tags using regex

s1 = re.compile("<script.*?</script>",re.DOTALL)
s2 = re.sub(s1, "", file)
file= s2
s1 = re.compile("<style.*?</style>",re.DOTALL)
s2 = re.sub(s1, "", file)
file= s2
#print(file)
##parse
##final result is wrapped in urwid scrollable (to deal with only plain text)
##





##recursive funcution
#in:  plain text / html + start of scope pointer
#out: urwid + pointer to end of scope in file (to not read same part twice)
def urwider (text, startlocation = 0):
    #print("urwider")
    ##parse starting from startlocation
    cursor = startlocation
    tempString = ""
    urwidArray = []
    while cursor < len(text)-1:
        #print(text[cursor] , cursor)

        

        ##if close tag "<" + "/"
        if (text[cursor] == "<") and (text[cursor + 1] == "/"):
            print("close tag!")
            print(tempString)
            values = tagBuilderFun(text,cursor)
            tag = values[0]
            cursor = values[1] - 1
            #print("values")
            #print(values)
            
            if len(tempString) > 0:
                urwidArray.append(urwid.Text(tempString))
                tempString = ""
            print(urwidArray)

            if len(urwidArray) > 0:
                urwidpile = urwid.Pile(urwidArray) 
            else:
                urwidpile = None
            return (urwidpile , cursor)
        ##if open tag "<"
        elif text[cursor] == "<":
            print("open tag!")
            
            
            ##look for ">"
            values = tagBuilderFun(text,cursor)
            tag = values[0]
            print("cursor update" , cursor , " to " , values[1])
            cursor = values[1]
            #print("values")
            #print(values)


            ##make urwid text widget for everything between last tag and current tag add to array
            #print(tempString)
            if len(tempString) > 0:
                urwidArray.append(urwid.Text(tempString))
                tempString = ""
            print(urwidArray)
            
            ##check tagBuilder <" "> against table
            ##call urwider()
            returned = urwider(text,cursor)
            print("END RECURSIVE")
            print(returned)
            if returned != None: #EOF
                if returned[0] != None:
                    urwidArray.append(returned[0])
            else:
                break
            cursor = returned[1]
        else:
            tempString = tempString + text[cursor]
        cursor = cursor + 1
    #EOF
    if len(urwidArray) > 0:
        urwidpile = urwid.Pile(urwidArray) 
    else:
        urwidpile = None
    print(urwidpile)
    return (urwidpile , cursor) 

def tagBuilderFun(text,cursor):
    tagBuilder = ""
    cursor = cursor + 1
    while text[cursor] != ">":
        #print(text[cursor])
        cursor = cursor + 1
        tagBuilder = tagBuilder + text[cursor-1]
    print("TAGBUILDER")
    print(tagBuilder)
    return tagBuilder,(cursor + 1)
        






final = urwid.ScrollBar(urwid.Scrollable(urwid.Filler(urwider(file)[0])))
loop = urwid.MainLoop(final)
loop.run()