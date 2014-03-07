from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target,key):
    length = len(target)        
    listst = []
    if find(target,key) == -1:      #Test for Base Case
        print "There are no instances of the substring in the target string"
    else:
        while find(target,key) > -1:
            listst = listst + [length - len(target) + find(target,key)]     #Add the length of the stripped string 
            target = target[find(target,key)+len(key):]                     #Strip the taarget down
    return listst
    
def constrainedMatchPair(match1, match2, length):
    filtered = []
    for a in match1:
        for b in match2:
            if a + length + 1 == b:             #Check for condition
                filtered = filtered + [a]
    return filtered
    
def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    allAnswers = []
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = str(key[:miss])
        key2 = str(key[miss+1:])
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        if len(key1) > 0:
            match1 = subStringMatchExact(target,key1)
        else:
            match1 = ()
        if len(key2) > 0:
            match2 = subStringMatchExact(target,key2)
        else: match2 = ()
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        print "executed"
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

#subStringMatchOneSub("atgacatgcacaagtatgcat", "atgc")



    







            



