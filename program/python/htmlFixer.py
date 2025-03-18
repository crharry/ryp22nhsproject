##########################
#To_Do____________________
#Deal with EOF cases (never closing tags)
#Deal with tags closing in child //see above
#






voidElements = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr']
removeBetween = ['script','style']
removeBetweenPointers = []
insertTagAt = []
##recursive
#in:  plain text / html + start of scope pointer
#out: pointer to end of scope in file (to not read same part twice)
def htmlFixer (text, startlocation = 0,parentTag=[None], grandparentTags = [None]):
    global insertTagAt
    ##parse starting from startlocation
    cursor = startlocation
    while cursor < len(text)-1:
        #print(text[cursor] , cursor)
        ##if close tag "<" + "/"
        ##if open tag "<"
        if text[cursor] == "<":
            if (text[cursor + 1] == "/"):
                print("close tag!")
                oldcursor = cursor
                values = tagBuilderFun(text,cursor)
                tag = values[0]
                cursor = values[1] - 1
                print(tag,parentTag)
                if tag == ("/"+parentTag[len(parentTag)-1]):
                    print("tag Successfully closed##########")
                    parentTag.pop()
                    return(cursor)
                else:
                    ##close tag does not match parent; add "closing tag" type before parent & open new after parent
                    print("NOT CLOSED##############################################################")
                    if (tag[1:] in parentTag):##is on wrong layer
                        print("close tag is in parent but not direct, likely close in child, treat as 'trailing'",tag[1:])
                        print(text[cursor:cursor+5])
                        openTagsToAppend = ""
                        closeTagsToAppend = ""
                        level = len(parentTag)-1
                        print(parentTag[level],tag)
                        while parentTag[level] != (tag[1:]):
                            print(parentTag[level])
                            openTagsToAppend = "<"+parentTag[level]+">" + openTagsToAppend
                            closeTagsToAppend = closeTagsToAppend + "</"+parentTag[level]+">"
                            level = level - 1
                        while level < len(parentTag) -1:
                            parentTag[level] = parentTag[level + 1]
                            level = level + 1
                        parentTag.pop()
                        print(insertTagAt, type(insertTagAt))
                        print("tags to add: ",[closeTagsToAppend,cursor-len(tag)],[openTagsToAppend,cursor+2])
                        if insertTagAt == None:
                            insertTagAt = [[closeTagsToAppend,cursor-len(tag)],[openTagsToAppend,cursor+2]]
                        else:
                            insertTagAt.append([closeTagsToAppend,cursor-len(tag)])
                            insertTagAt.append([openTagsToAppend,cursor+2])
                        #insertTagAt.append([tagsToAppend[0],cursor-len(tag)-1])
                    else:##is "random close"
                        print("close tag is not in parent and not direct, therefore random close",tag[1:])
                        removeBetweenPointers.append([oldcursor,cursor+1])



                #print("values")
                #print(values)
            else:
                print("open tag!")
                ##look for ">"
                values = tagBuilderFun(text,cursor)
                tag = values[0]
                #print("cursor update" , cursor , " to " , values[1], "because of tag: " , tag)
                oldcursor = cursor # start of tag, used to remove unsupported tags
                cursor = values[1]
                #print("values")
                #print(values)

                
                ##make tag similar to closetag
                tag = tag.split(" ",2)[0]
                print("modified open tag = " , tag)
                if tag in voidElements:
                    print("VOID" , tag)
                    cursor = cursor -1
                elif tag in removeBetween:
                    cursor = findCloseTag(text, cursor, tag)
                    print("remove: " , tag , " @  ", oldcursor, "to " , cursor)
                    removeBetweenPointers.append([oldcursor,cursor])
                    cursor = cursor -1
                else:
                    ##call htmlFixer()
                    print("parentTag tags: ",parentTag)
                    if parentTag[0] == None:
                        parentTag[0] = tag
                    else:
                        parentTag.append(tag)
                    returned = htmlFixer(text,cursor,parentTag)
                    #print("END RECURSIVE")
                    print(returned)
                    if returned != None: #EOF
                        print("")
                    else:
                        break
                    cursor = returned
            
        cursor = cursor + 1
    #EOF

def tagBuilderFun(text,cursor):
    tagBuilder = ""
    cursor = cursor + 1
    while text[cursor] != ">":
        #print(text[cursor])
        cursor = cursor + 1
        tagBuilder = tagBuilder + text[cursor-1]
    #print("TAGBUILDER",tagBuilder)
    return tagBuilder,(cursor + 1)

def findCloseTag(text, cursor,openTag):##USED FOR REMOVING TAGS
    found = False
    while not (found):
        while text[cursor] != "<":
            cursor = cursor + 1
            #print(text[cursor])
        if text[cursor+1] == "/":
            closeTag = tagBuilderFun(text,cursor)
            #print(closeTag)
            if ("/" + openTag) == closeTag[0]:
                print(("/" + openTag) , closeTag)
                cursor = closeTag[1] + 1
                found = True
                break
        else:
            cursor = cursor + 1
    #print(text[cursor-1])
    return cursor-1

#file = open("../node/index.html","r").read()
#print(htmlFixer(file,startlocation = 0))

print(removeBetweenPointers)
print(insertTagAt)
def removeFixTags(text,removeBetweenPointers,insertTagAt):
    oldCursor = len(text) + 1
    oldtext = text
    print("original len: " , oldCursor)
    x = len(removeBetweenPointers)-1
    while x >= 0:
        tempText = text[removeBetweenPointers[x][1]:]
        text = text[:removeBetweenPointers[x][0]] + tempText
        x = x - 1
    print(text)
    print("new len: " , len(text))
    print("Fixing tags")

    newcursor = len(text)
    x = len(removeBetweenPointers) - 1
    y = len(insertTagAt) - 1
    if y > 0:
        while oldCursor > 0 :
            #print(oldtext[oldCursor-1])
            print(newcursor,oldCursor,y)

            if oldCursor == insertTagAt[y][1]:
                print("inserted section", insertTagAt[y][1])
                insertTagAt[y][1] = newcursor
                newcursor = newcursor + 1
                oldCursor = oldCursor + 1
                y = y - 1
            if removeBetweenPointers[x][1] >= oldCursor and (x >= 0):
                print("cursor skip :", oldCursor , oldCursor - (removeBetweenPointers[x][1] - removeBetweenPointers[x][0]-1),  removeBetweenPointers[x], "next insert at:", insertTagAt[y][1])
                oldCursor = oldCursor - (removeBetweenPointers[x][1] - removeBetweenPointers[x][0])
                oldCursor = oldCursor + 1
                print("removed section")
                x = x - 1


            newcursor = newcursor - 1
            oldCursor = oldCursor - 1
    print(removeBetweenPointers)



    counter = len(insertTagAt)-1
    print(insertTagAt)
    while counter >= 0:
        text = text[:insertTagAt[counter][1]] +insertTagAt[counter][0] + text[insertTagAt[counter][1]:]
        counter = counter - 1
    print("new len: " , len(text))
    print(text)
    removeBetweenPointers.clear()
    insertTagAt.clear()
    return text

#removeFixTags(file,removeBetweenPointers,insertTagAt)

def htmlFixerMain(file):
    htmlFixer(file,startlocation = 0)##to find errors
    fixed = removeFixTags(file,removeBetweenPointers,insertTagAt)#to correct errors

    return fixed


