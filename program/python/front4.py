import urwid, requests
from htmlFixer import htmlFixerMain
from specialElements import BoxButton,a
voidElements = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr',"!doctype"]
specialElements = ['a']#tags not treated as text
specialObjects = [a("placeholder",[urwid.Text("placeholder")])]




## inputs  : output text from htmlfixer, pointer to begining of tags children
## outputs : array of urwid elements (pile,text,'link')
def urwider(text, startlocation = 0):
    print("urwider")
    # find tag
    # from start(or prevtag) put into text element
    # add text element to array
    # if void tag, run void tag handler   ### nothing for now
    # if open tag, urwider(pointer to end of open tag)
    # if close tag, return urwid[], unless theres only 1 child then return urwid. urwid type depends on tag

    cursor = startlocation
    tempString = ""##plain text string, from inbetween tags
    urwidArray = []##array of urwid widgets, to be added to a pile and returned
    while cursor < len(text):
        print(cursor)
        
        if text[cursor] == "<":
            ##turn add tempString to urwid array
            if len(tempString) > 0:
                #print(tempString)
                urwidArray.append(urwid.Text(tempString))
                tempString = ""
            #print("tag")
            if text[cursor + 1] == "/":
                tag = tagBuilderFun(text,cursor)
                cursor = tag[1]  -1
                tag = tag[0]
                print("close Tag",tag)
                #return children
                print(urwidArray,"returning")

                if len(urwidArray) == 0:
                    return None,cursor
                else:
                    return urwidArray,cursor


                ######################################################close tag ↑↑↑↑
            else:
                ######################################################open  tag ↓↓↓↓
                tag = tagBuilderFun(text,cursor)
                cursor = tag[1]
                tag = tag[0]
                print("open Tag",tag)
                ##tag handlers ↓↓↓↓
                ##check for special tag
                ##check for void tag
                #call urwid to urwidify children
                tagShort = tag.split(" ",1)
                print(tagShort)
                if tagShort[0] in specialElements:
                    returned = SpecialTag(tagShort,tag,cursor,text)
                    cursor = returned[1]
                    urwidArray.append(returned[0][0])


                elif tagShort[0] in voidElements:
                    cursor -=1
                else:
                    returned = DefaultOpenTag(text,cursor)##[urwidarray,cursor]
                    if returned[0] == None:##handle no children
                        cursor = returned[1]
                    else:
                        urwidArray.append(returned[0])
                        cursor = returned[1]
                ######################################################open  tag ↑↑↑↑
        else:
            ##not a tag, plain text
            tempString += text[cursor]
        cursor += 1
    ##End Of File
    print("eof")
    if len(tempString) > 0:
        urwidArray.append(urwid.Text(tempString))
    return(urwid.Filler(urwid.Pile(urwidArray))),len(text)-1


def DefaultOpenTag(text,cursor):
    print("this is a standard tag, treated as plain Text, however it may be within a more *special* tag")
    returned = urwider(text,cursor)##[urwidarray,cursor]
    urwidArray = returned[0]
    cursor = returned[1]
    if urwidArray == None:
        return None, cursor
    elif issubclass(type(urwidArray),urwid.Widget):#EOF
        return urwidArray,cursor
    elif len(urwidArray) == 1:
        return urwidArray[0],cursor
    elif len(urwidArray) > 1:
        pile = urwid.Pile(urwidArray)
        return pile,cursor

        
    #return urwider(text,cursor)##[urwidarray,cursor]

def SpecialTag(tagShort,tag,cursor,text):
    print("this is a special" , tagShort[0], "tag")
    ##check tag type,
    index = specialElements.index(tagShort[0])
    print(index)
    ## find object type
    #print(specialObjects[index])
    elementType = type(specialObjects[index])
    ## create object
    #####################################################################################broken__ assuming plain text only 
    ## populate with children (call urwid, depending on type)
    if specialObjects[index].canHaveChildren:
        childpile = []
        returned = urwider(text,cursor)
        print(returned[0])
        cursor = returned[1]
        if len(returned[0]) > 0:
            for x in (returned[0]):
                childpile.append(x)
            newObj = elementType(url = "url",children=childpile)
            #newObj = aDemo(url = "url",children=childpile)

    ##newObj.get();##urwid pile containing children
    if specialObjects[index].hasListener:
        print("adding listener to ",newObj)
        newcursor = 0
        while newcursor < len(tag)-4:
            print(tag[newcursor])
            if tag[newcursor:newcursor+4].lower() == "href":

               href = tag[newcursor+4:].split(" ")[0].strip(" ").split("=")[1]
               break
            newcursor += 1 
        href = href.strip('"').strip("'")
        print(href)
        newObj.setUrl(href)
        
    
    if specialObjects[index].canHaveChildren:#pile
        newObj.pileChildren()
        if specialObjects[index].hasListener:
            urwid.connect_signal(newObj.get()[1],"click", linkClicked,href)
    
    return newObj.get(),cursor
    ##return urwid object , cursor

def VoidTag(tag):
    print("void tags are not supported... yet")


def linkClicked(*args, **kwargs):
    #print(*args, **kwargs)
    URL = args[1]
    print("url = ",args[1])
    request = requests.get(URL)
    print(request.text)
    text = htmlFixerMain(request.text)
    urwidFormattedPage = urwider(text,0)[0]
    print(text)
    print(urwidFormattedPage)
    loop.widget = urwid.ScrollBar(urwid.Scrollable((urwidFormattedPage)))
    loop.draw_screen()
    


def tagBuilderFun(text,cursor):
    tagBuilder = ""
    cursor = cursor + 1
    while text[cursor] != ">":
        #print(text[cursor])

        cursor = cursor + 1
        tagBuilder = tagBuilder + text[cursor-1]
    #print("TAGBUILDER",tagBuilder)
    return tagBuilder,(cursor + 1)




#print(urwider("<html><p>paragraph<b>bold</b></p></html>",0))

loop = urwid.MainLoop(urwid.Filler(urwid.Text("loading...")))



urwidFormattedPage = urwider('<html><meta><p>paragraph<b>bold</b>after bold</p><a href="https://www.google.com">this is a link</a>hello</html>hi',0)[0]
loop = urwid.MainLoop(urwidFormattedPage)
loop.run()
linkClicked([None,"https://www.google.com"],[None])


## button demo
#URL = "https://www.google.com"
#linkText = "www.google.com"
#button = urwid.Button(urwid.Text("[" + linkText + "]"))
#urwid.connect_signal(button,"click", linkClicked,URL)
#button = urwid.AttrMap(button, '', 'highlight')
#urwidUI = urwid.ScrollBar(urwid.Scrollable(urwid.Filler(button)))
#loop = urwid.MainLoop(urwidUI)
#loop.run()
