from string import *
from globalfunctions import *
def subStringMatchExact(target,key):
    length = len(target)        
    listst = []
    if find(target,key) == -1:      #Test for Base Case
        print "There are no instances of the substring in the target string"
        return None
    else:
        while find(target,key) > -1:
            listst = listst + [length - len(target) + find(target,key)]     #Add the length of the stripped string 
            target = target[find(target,key)+len(key):]                     #Strip the taarget down
        return listst
        
target = readVal(str, "Please enter the target string ", "Oops! That's not a string! Try again")
key = readVal(str, "Please enter the Key string ", "Oops! That's not a string! Try again")
print "The number of instances of the substring in the target string is", subStringMatchExact(target,key)
