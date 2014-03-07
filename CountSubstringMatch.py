from globalfunctions import *
from string import *
def countSubStringMatch(target,key):
    count = 0
    while find(target,key) > -1:
        count += 1
        target = target[find(target,key)+len(key):]
    print count


def countSubStringMatchRecursive (target, key):
    if find(target,key) == -1:
        return 0
    else:
        return 1 + countSubStringMatchRecursive (target[find(target,key)+len(key):], key)
                

    
target = readVal(str, "Please enter the target string ", "Oops! That's not a string! Try again")
key = readVal(str, "Please enter the Key string ", "Oops! That's not a string! Try again")
print "The number of instances of the substring in the target string is", countSubStringMatchRecursive(target,key)


