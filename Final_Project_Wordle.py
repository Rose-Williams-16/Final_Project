def format(): # This defines a function that ensures the guess is an actual word of the proper length.
    while True: # This repeats if the guess doesn't meet the requirements.
        guess = input() # The user inputs a guess here.
        if five_all_letters(guess) and real_word(guess): # If both requirements are true, the while loop breaks.
            break
    return guess # The user's guess is returned.
def real_word(guess): # This defines a function that ensures the guess is one of the words in the list from the database.
    is_real_word = False # The variable determining the guess's status is set to false.
    for word in range(len(word_list)): # This iterates over the entire list (>2000 words!)
        if guess.lower() == word_list[word]: # This compares the guess (case irrelevant) to each word in the list.
            is_real_word = True # If the guess and word match, the variable determining the guess's status is set to true.
    if is_real_word == False: # A message pops up if the guess isn't present, informing the user that their guess is not valid.
        print("I'm sorry, that isn't a word in the database.\nPlease try again:")
    return is_real_word # The condition of whether or not the word is in the list is returned.
def five_all_letters(guess): # This defines a function that ensures the guess is the proper length and only contains letters.
        if len(guess) == 5 and guess.isalpha(): # This is the correct format.
            return True # True is returned for the correct format.
        elif guess.isalpha() == False: # This case happens when the guess contains non-letter characters (including spaces and underscores).
            print("Make sure your word only contains letters!\nPlease try again:")
            return False # False is returned for the incorrect format.
        elif len(guess) != 5: # This case happens when the guess only contains letters, but it contains the wrong number of them.
            print("Make sure your word is five letters long!\nPlease try again:")
            return False # Again, false is returned for the incorrect format.
        else: # This case should never happen, but just in case, I've added a general statement that the format of the guess is incorrect.
            print("Incorrect format.\nPlease try again:")
            return False
def play_again(): # This defines a function that asks the user if they want to play another round.
    print("Would you like to play again?\nAnswer yes or no:")
    while True: # This repeats if the user's answer isn't yes or no.
        global playing # This makes the possible change in the variable "playing" apply to the global variable.
        answer = input() # The user inputs their answer here.
        if answer.lower() == "yes": # If the user inputs yes (irrelevant of case), the while loop breaks, but the value of the variable "playing" is not changed.
            break
        elif answer.lower() == "no": # If the user inputs no (again, irrelevant of case), the variable "playing" is set to false and the while loop breaks.
            playing = False
            break
        else: # If neither yes nor no is input, the user is again prompted to answer yes or no, and the while loop repeats.
            print("Please answer yes or no:")
from pathlib import Path # This module must be imported in order to work with the file containing the 5-letter word database.
import random # This module must be imported in order to have the program select a random word from the database.
word_file = Path("5_letters.csv") # This is the database file, so long as it's in the same folder as the program.
with open(word_file) as f: # This opens the database file in read mode, in a way that doesn't require it to be closed later on.
    next(f) # This skips the first line of the database file (which is just the numbers 1,2,3,4,5, not a word).
    word_list = f.readlines() # This creates a list where each element is a line of the file (the words, but as individual characters separated by commas).
for k in range(len(word_list)): # This iterates over the entire list that was just created.
    word_list[k] = word_list[k].strip().replace(",", "") # This removes the commas and newline characters from each element, formatting them as words.
playing = True # The variable "playing" is set to "True".
print("Welcome to Wordle!") # When the user begins playing, they are greeted by the program.
while playing == True: # This only becomes false, breaking the loop, if the user inputs "no" to the question of if they want to play again.
    word_index = random.randrange(len(word_list)) # This selects a random index from the list of words.
    word = word_list[word_index] # The correct answer is set as the word from the list whose index was just randomly selected.
    print("Guess a five-letter word:") # The user is asked to guess a word.
    for i in range(6): # Wordle allows a maximum of 6 guesses, so the loop runs up to 6 times.
        guess = format().lower() # This calls the "format" function, checking the word's validity, and also makes case irrelevant.
        if guess == word: # This case is if the guess matches the word (i.e. is correct).
            if i == 0: # This distinction is for grammatical purposes -- "try" versus "tries".
                print("You correctly guessed " + word + " in 1 try!")
            else: # Remember that the actual number of guesses is one more than the index of iteration.
                print("You correctly guessed " + word + " in " + str(i+1) + " tries!")
            break # This breaks the for loop, since the correct answer has been guessed.
        else: # This case is if the guess does not match the word (i.e. is incorrect).
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
                                guess_copies += 1 # 1 is added to the number of copies for every instance the current letter matches a letter in the range (it will always be at least 1).
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
            else: # If no attempts remain, the user is told that they've run out of guesses and what the correct answer was. The for loop does not repeat.
                print("Sorry, you've run out of tries!\nThe correct answer was " + word + ".")
    play_again() # This calls the "play_again" function, asking the user whether they want the game to repeat.
print("Goodbye!") # After the user decides to stop playing, they are given a farewell.