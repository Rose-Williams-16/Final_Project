def format():
    while True:
        guess = input()
        if five_all_letters(guess) and real_word(guess):
            break
    return guess
def real_word(guess):
    is_real_word = False
    for word in range(len(word_list)):
        if guess.lower() == word_list[word]:
            is_real_word = True
    if is_real_word == False:
        print("I'm sorry, that isn't a word in the database.\nPlease try again:")
    return is_real_word
def five_all_letters(guess):
        if len(guess) == 5 and guess.isalpha():
            return True
        elif guess.isalpha() == False:
            print("Make sure your word only contains letters!\nPlease try again:")
            return False
        elif len(guess) != 5:
            print("Make sure your word is five letters long!\nPlease try again:")
            return False
        else:
            print("Incorrect format.\nPlease try again:")
            return False
def play_again():
    print("Would you like to play again?\nAnswer yes or no:")
    while True:
        global playing
        answer = input()
        if answer.lower() == "yes":
            break
        elif answer.lower() == "no":
            playing = False
            break
        else:
            print("Please answer yes or no:")
from pathlib import Path
import random
word_file = Path("5_letters.csv")
with open(word_file) as f:
    next(f)
    word_list = f.readlines()
for k in range(len(word_list)):
    word_list[k] = word_list[k].strip().replace(",", "")
playing = True # The variable "playing" is set to "True".
print("Welcome to Wordle!") # When the user begins playing, they are greeted by the program.
while playing == True: # This only becomes false, breaking the loop, if the user inputs "no" to the question of if they want to play again.
    word_index = random.randrange(len(word_list))
    word = word_list[word_index]
    print("Guess a five-letter word:")
    for i in range(6): # Wordle allows a maximum of 6 guesses, so the loop runs up to 6 times.
        guess = format().lower() # This makes case irrelevant.
        if guess == word: # This is if the guess matches the word (i.e. is correct).
            if i == 0: # This distinction is for grammatical purposes -- "try" versus "tries".
                print("You correctly guessed " + word + " in 1 try!")
            else: # Remember that the actual number of guesses is one more than the index of iteration.
                print("You correctly guessed " + word + " in " + str(i+1) + " tries!")
            break # This breaks the for loop, since the correct answer has been guessed.
        else:
            for letter in range(5): # This iterates over the 5 letters in each word.
                if guess[letter] == word[letter]: # This compares each letter in the guess to the letter in the answer that's in the corresponding position.
                    print(guess[letter] + " is present and in the right place.") # If they match, the user is informed that that letter is in the right place.
                else:
                    present = False # This sets the presence of a particular letter to "False".
                    for j in range(5):
                        if guess[letter] == word[j]:
                            present = True # The presence is changed to "True" if the letter in question matches a letter within the answer.
                    if present == True: # This is what happens if the guessed letter is in the answer.
                        guess_copies = 0 # This sets the number of times the letter in question appears in each word to 0.
                        word_copies = 0
                        for m in range(letter+1): # This iterates ONLY FROM THE BEGINNING THROUGH THE CURRENT LETTER.
                            if guess[m] == guess[letter]:
                                guess_copies += 1 # 1 is added to the number of copies for every instance the current letter matches a letter in the range (it will always be at least 1)
                        for n in range(5): # This iterates OVER THE ENTIRE WORD.
                            if word[n] == guess[letter] and word[n] != guess[n]:
                                word_copies += 1 # 1 is added to the number of copies for every instance the current letter matches a letter in the range, EXCEPT when they are in the same position (that case was covered earlier and we don't want it considered here).
                        if guess_copies <= word_copies: # If there are fewer repetitions of the letter in the guess (so far!) than the answer, the user is told that the letter is present but in the wrong place.
                            print(guess[letter] + " is present, but in the wrong place.")
                        else: # Otherwise, the user is told that the letter is not present.
                            print(guess[letter] + " is not present.")
                    else: # This is what happens if the guessed letter is not in the answer.
                        print(guess[letter] + " is not present.")
            if i < 5: # If more attempts remain, the user is given an opportunity to guess again, and the for loop repeats.
                print("Guess again:")
            else: # If no attempts remain, the user is told that they've run out of guesses and what the correct answer is. The for loop does not repeat.
                print("Sorry, you've run out of tries!\nThe correct answer was " + word + ".")
    play_again()
print("Goodbye!") # After the user decides to stop playing, they are given a farewell.