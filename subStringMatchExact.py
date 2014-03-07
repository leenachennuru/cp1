from string import *
def subStringMatchExact(target,key):
    length = len(target)
    listst = []
    if find(target,key) == -1:
        print "There are no instances of the substring in the target string"
        return None
    else:
        while find(target,key) > -1:
            listst = listst + [length - len(target) + find(target,key)]
            target = target[find(target,key)+len(key):]
        print "The list of instances of the substring in the target string is", listst
        
