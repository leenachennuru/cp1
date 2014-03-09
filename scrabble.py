
import random
import string
from globalfunctions import *

VOWELS = 'aeiou'                                #Define Vowels and Consonents to improve the probality of forming a word from a hand.
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7                                    #Variable determining size of the hand

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}                           #Scrabble letter values

WORDLIST_FILENAME = "words.txt"         #Import words.txt from the folder

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)        #Open File
    # wordlist: list of strings
    wordlist = []
    for line in inFile:                         
        wordlist.append(line.strip().lower())           #Create Array
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

#
def get_word_score(word, n):                        # Scoring a word
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for a in word:
        score = score + SCRABBLE_LETTER_VALUES[a]       #Calculate word score
    if len(word) == n:                          
        score += 50                                 #50 bonus points if you use up all the letters of your hand.
    return score
    # TO DO ...

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line
    return None

#
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]                     #atleast n/3 vowels selected randomly
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):                                      #Remaining Consonents selected randomly 
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
#
def update_hand(hand, word):                                            # Update a hand by removing letters
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    updated_hand = {}
    for letter in hand.keys():
        updated_hand[letter] = hand.get(letter, 0)                      #Initialize update hand to hand
    for letter in word:
        updated_hand[letter] = updated_hand.get(letter, 0) - 1          #Remove letters in word from updated hand
        if updated_hand[letter] == 0:                               
            del updated_hand[letter]                                    
    return updated_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    value = True
    updated_hand = update_hand(hand, word)
    for a in updated_hand:
        if updated_hand[a] < 0:                             #If a letter in the word is not present in the hand, return False
            value = False
            break
    else:
        for b in word_list:                                 #If a word is not in the word list. Return False
            if b == word:
                value = True
    return value
        

#
#
    

def play_hand(hand, word_list):                             # Playing a hand
    word_score = 0
    Tot_score = 0
    end_game = False
    display_hand(hand)
    while len(hand) > 0:
        while True:
            word = raw_input("Please enter your word or enter '.' if you wish to end the game ")        #Input Word
            if word == '.':                                                             
                end_game = True                                                                         #End of game if period is entered
                break
            value = is_valid_word(word, hand, word_list)                                                #Check if the word is valid
            if value == True:
                break
            else:
                print "Oops! You made a boo boo. That's not a word. Try again!"                         #Throw error if its an invalid word
            
        if end_game == True:                                                                            #Check to see if game has ended
            print "Your game has ended"
            break
        
        else:
            word_score = get_word_score(word, len(hand))                                                #Calculate word score
            Tot_score = Tot_score + word_score                                                          #Total Score
            hand = update_hand(hand,word)                                                               #update hand by removing letters from word
            new_hand = deal_hand(len(word))                                                         #deal a new hand to fill in the letters of the word.
            print "The score for the current word is ", word_score
            print "Your total score so far is", Tot_score
            print len(word), "new letters have been added to your hand"
            print "The new letters added to your hand are"
            display_hand(new_hand)
            display_hand(hand)
            for elem in new_hand:
                hand[elem] = hand.get(elem,0) + new_hand[elem]                  #Add the new dealt hand to the updated hand
            print "Your updated hand is"
            display_hand(hand)
                
    else:
        print "You have used up all the letters in your hand. Your game ends here"

    print "Your total score for this game is", Tot_score

#
# 
def play_game(word_list):                                   # Playing a game
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to get a new hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

