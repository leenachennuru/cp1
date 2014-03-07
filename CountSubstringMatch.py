from globalfunctions import *
from string import *
def countSubStringMatch(target,key):
    count = 0                                           #Initialize Counter
    if find(target,key) == -1:
        print "There are no instances of this substring in the target string"   #Base Case
    else:
        while find(target,key) > -1:
            count += 1                                      #Increment the counter
            target = target[find(target,key)+len(key):]     #Strip the traget down
        print count


def countSubStringMatchRecursive (target, key):
    if find(target,key) == -1:          #Base Case
        return 0
    else:
        return 1 + countSubStringMatchRecursive (target[find(target,key)+len(key):], key) #Apply the function recursively on the smaller string
                

    
target = readVal(str, "Please enter the target string ", "Oops! That's not a string! Try again")
key = readVal(str, "Please enter the Key string ", "Oops! That's not a string! Try again")
print "The number of instances of the substring in the target string is", countSubStringMatchRecursive(target,key)


