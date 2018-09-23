
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
 
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
#    print("  ", len(wordlist), "words loaded.")
    return wordlist




def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



def is_word_guessed(secret_word, letters_guessed):


    if set(letters_guessed).issuperset(set(secret_word)) == True:
        print("Woohoo you won! The word was", secret_word_display,"!")
        return True
    else: 
        return False
        
     
            



def get_guessed_word(secret_word, letters_guessed):
  
    
    guessed_word=secret_word[:]
#
    
    for i in range(len(secret_word)):
        if guessed_word[i] not in letters_guessed:
            guessed_word[i] = "_"
    return guessed_word
            

def get_available_letters(letters_guessed):
    
    
    all_letters="abcdefghijklmnopqrstuvwxyz"
    all_letters_list=list(all_letters)
    
    
    for i in letters_guessed:
        if i in all_letters_list:
            all_letters_list.remove(i)
    return all_letters_list
    



#def hangman(secret_word):
#    
#    guesses=6
#    oops_counter=3
#    print("Welcome to the game of Hangman!\nI am thinking of a word that is",
#          len(secret_word), "letters long\n----------\nYou have", guesses,"guesses left.\n"
#          "Available letters:", get_available_letters(letters_guessed))
#    
#    while is_word_guessed(secret_word, letters_guessed) == False:
#        x=str(input("Please guess a letter:"))
#        y=(x.lower())
#        z=list(y)
#        if z[0] in secret_word and z[0] not in letters_guessed:
#            letters_guessed.append(z[0])
#            print("Good guess:", " ".join(get_guessed_word(secret_word, letters_guessed)),
#            "\nYou have", guesses, "guesses remaining.\n-----------------------"
#            "\nAvailable letters:", get_available_letters(letters_guessed))
##                                        
#        elif z[0] in secret_word and z[0] in letters_guessed and oops_counter > 0:
#            print("Oops... you already guessed that letter...I give you", (oops_counter-1)," more"
#                  " warnings\nAvailable letters:", get_available_letters(letters_guessed),
#                  "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
#            oops_counter-=1
#        elif z[0] not in list("abcdefghijklmnopqrstuvwxyz") and oops_counter > 0:
#            print("Oops! That is not a letter. I give you", (oops_counter-1)," more"
#                  " warnings\nAvailable letters:", get_available_letters(letters_guessed),
#                  "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
#            oops_counter-=1
#        elif z[0] in list("abcdefghijklmnopqrstuvwxyz"):
#            letters_guessed.append(z[0])
#            guesses-=1
#            if guesses == 0:
#                print("Oh... seems like you are out of luck... The word was", 
#                      secret_word_display,"Better luck next time...")
#                break
#            else:
#                print("Oopsy-doodles!, that is not in the word! You have", guesses,
#                      "guesses remaining.\n---------------------\n"
#                      "Available letters:", get_available_letters(letters_guessed),
#                         "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
#        else:
#            guesses-=1
#            if guesses == 0:
#                print("Oh... seems like you are out of luck... The word was", 
#                      secret_word_display,"Better luck next time...")
#                break
#            else:
#                print("Oopsy-doodles!, that is not in the word! You have", guesses,
#                      "guesses remaining.\n---------------------\n"
#                      "Available letters:", get_available_letters(letters_guessed),
#                         "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
#    
#    


#wordlist=load_words()
#secret_word_display=choose_word(wordlist)
#secret_word_display="fart"
#secret_word=list(secret_word_display)
#
#letters_guessed=list()
#x=(is_word_guessed(secret_word, letters_guessed))
#guessed_word1=" ".join(get_guessed_word(secret_word, letters_guessed))
#available_letters=get_available_letters(letters_guessed)
#guesses=6
##hangman (secret_word)
#my_word=guessed_word1
#other_word=wordlist




def match_with_gaps(my_word, other_word):
    
    my_word=''.join(get_guessed_word(secret_word, letters_guessed))
    true_counter=0
    
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == other_word[i] or my_word[i] == "_":
                true_counter+=1
        if true_counter == len(my_word):
            return True
        else:
            return False
    else:
        return False


my_word=''.join(get_guessed_word(secret_word, letters_guessed))
    
def show_possible_matches(my_word):
  
    possible_matches= list()
    possible_matches_clone=possible_matches[:]
    
    for i in wordlist:
        if match_with_gaps(my_word, i) == True:
            possible_matches_clone.append(i)
        
    
    print(' '.join(possible_matches_clone))
     



def hangman_with_hints(secret_word):

    guesses=6
    oops_counter=3
    print("Welcome to the game of Hangman!\nI am thinking of a word that is",
          len(secret_word), "letters long\n----------\nYou have", guesses,"guesses left.\n"
          "Available letters:", get_available_letters(letters_guessed))
    
    while is_word_guessed(secret_word, letters_guessed) == False:
        x=str(input("Please guess a letter:"))
        y=(x.lower())
        z=list(y)
        if z[0] == "*":
            print("The possible matches are:")
            show_possible_matches(my_word)
            print("\nYou have", guesses, "guesses remaining.\n-----------------------"
            "\nAvailable letters:", get_available_letters(letters_guessed))
        elif z[0] in secret_word and z[0] not in letters_guessed:
            letters_guessed.append(z[0])
            print("Good guess:", " ".join(get_guessed_word(secret_word, letters_guessed)),
            "\nYou have", guesses, "guesses remaining.\n-----------------------"
            "\nAvailable letters:", get_available_letters(letters_guessed))
#                                        
        elif z[0] in secret_word and z[0] in letters_guessed and oops_counter > 0:
            print("Oops... you already guessed that letter...I give you", (oops_counter-1)," more"
                  " warnings\nAvailable letters:", get_available_letters(letters_guessed),
                  "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
            oops_counter-=1
        elif z[0] not in list("abcdefghijklmnopqrstuvwxyz") and oops_counter > 0:
            print("Oops! That is not a letter. I give you", (oops_counter-1)," more"
                  " warnings\nAvailable letters:", get_available_letters(letters_guessed),
                  "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
            oops_counter-=1
        elif z[0] in list("abcdefghijklmnopqrstuvwxyz"):
            letters_guessed.append(z[0])
            guesses-=1
            if guesses == 0:
                print("Oh... seems like you are out of luck... The word was", 
                      secret_word_display,"Better luck next time...")
                break
            else:
                print("Oopsy-doodles!, that is not in the word! You have", guesses,
                      "guesses remaining.\n---------------------\n"
                      "Available letters:", get_available_letters(letters_guessed),
                         "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
        else:
            guesses-=1
            if guesses == 0:
                print("Oh... seems like you are out of luck... The word was", 
                      secret_word_display,"Better luck next time...")
                break
            else:
                print("Oopsy-doodles!, that is not in the word! You have", guesses,
                      "guesses remaining.\n---------------------\n"
                      "Available letters:", get_available_letters(letters_guessed),
                         "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))

wordlist=load_words()
secret_word_display=choose_word(wordlist)
secret_word=list(secret_word_display)
letters_guessed=list()
guessed_word1=' '.join(get_guessed_word(secret_word, letters_guessed))
available_letters=get_available_letters(letters_guessed)
guesses=6
hangman_with_hints(secret_word)



