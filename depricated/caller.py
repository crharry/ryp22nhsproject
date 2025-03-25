from front2 import *
import sys
###for front2.py
print ('argument list', sys.argv)

opened = True
defaultPage = sys.argv[1]
if opened:
    opened = False
    openLink(defaultPage)
