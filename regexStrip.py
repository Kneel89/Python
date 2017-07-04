import re
import pyperclip

def strip(x,y=None):
    if y != None:
        xRegex = re.compile(*y)
        print(xRegex.sub('',str(x)))
    elif y == None:
        xRegex = re.compile(r'^\s*|\s*$')
        print(xRegex.sub('',str(x)))
        #^spam means the string must begin with spam.
        #spam$ means the string must end with spam.
        #\s matches a space

strip('  dfsdf    s','d')

