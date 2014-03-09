# Problem Set 5: Ghost
# Name: Leena Suresh
# Collaborators: None
# Time: 30 mins
#

import random

# -----------------------------------

import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def is_an_alphabet(char):
    if char in string.ascii_letters:
        return True
    
    else:
        return False
        

def is_a_valid_word(word):
    value = None
    for a in wordlist:
        if a == word:
            value = True
    return value
    
    
def words_start_with_str(string):
    value = None
    for a in wordlist:
        if string == (a[:len(string)]):
            value = True
            break
    else:
        value = False
    return value

def update_string(char, string):
    string += char
    return string

def play_turn(n):
    player = 1
    current_word_fragment = ''
    while player < n + 1 : 
        while True:
            i = str(player)
            concat_string = "Player" + " " + i + " " + "says letter "
            char = raw_input(concat_string)
            if is_an_alphabet(char):
                break
            else:
                print "You have not entered an alphabet. Please try again. "             
        current_word_fragment = update_string(char,current_word_fragment)
        if (words_start_with_str(current_word_fragment) == False):
            print "Player", player ,"loses. There are no words which start with", current_word_fragment
            break
        if len(current_word_fragment) > 3:
            if is_a_valid_word(current_word_fragment):
                print "Player", player ,"loses. You formed a word with more than 3 letters."
                break
        if player == n:
            player = 1
        else:
            player += 1
        print "Player", player,"'s turn."
    
    
        

    
def ghost(n):
    print "Welcome to Ghost! "
    print "Player 1 goes first"
    print "Current word Fragment = ''"
    play_turn(n)

    
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg)
        try:
            val = valType(val)
            return val
        except:
            print(errorMsg)
    return val

n = readVal(int, "Please enter the number of players ", "That is not an Integer. Type in an integer value")

ghost(n)
        
        
        
        
    
        
    
