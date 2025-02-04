import time
import os
import sys
#print ('argument list', sys.argv)
#print (os.name)


def search(url):
    if os.name == "posix":
        #search
        print('curl ' + ' -o ../node/index.html ' + url)
        os.system('curl ' + ' -o ../node/index.html ' + url)
        #update current json
        os.system('node ../node/node.js ../node/index.html > ../node/test.json')
        
        ##os.system('python3 front2.py')
        
    if os.name == "nt":
        #search
        print('curl ' + url + ' -o ../node/index.html')
        os.system('curl ' + ' -o ../node/index.html ' + url)
        time.sleep(2) 
        #update current json
        os.system('node ../node/node.js ../node/index.html > ../node/test.json')
        os.system('python front2.py')






##
##if os.name == "posix":
##    #search
##    if len(sys.argv) > 1:
##        os.system('wget ' + sys.argv[1] + ' -O ../node/index.html')
##    else:
##        site = input("url... ")
##        site = "https://" + site
##        os.system('wget ' + site + ' -O ../node/index.html')
##    #update current json
##    os.system('node ../node/node.js ../node/index.html > ../node/test.json')
##    os.system('python3 front.py')
##
##if os.name == "nt":
##        #search
##    if len(sys.argv) > 1:
##        os.system('curl ' + sys.argv[1] + ' -o ../node/index.html')
##    else:
##        site = input("url... ")
##        if len(site) > 2:
##            site = "https://" + site
##            os.system('curl ' + site + ' -o ../node/index.html')
##    #update current json
##    os.system('node ../node/node.js ../node/index.html > ../node/test.json')
##    os.system('python front.py')
