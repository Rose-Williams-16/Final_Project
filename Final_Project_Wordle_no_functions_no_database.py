# This is a draft. It still needs to be converted into a format that includes functions.
# Also, there needs to be a list of words for the program to randomly select from.
# (In the meantime, feel free to change the word given in the word = "hello" statement.
# Make sure it's still 5 letters long. Repeated letters make for interesting cases!)
# This list will also be used to verify that user-input guesses are actual words.
# The code for that will look something like this:
# word_list = (whatever text file has been read by the program)
# word = word_list[rand.range(0, len(word_list))]
#real_word = False
#for w in range(len(word_list)):
#    if guess == word_list[w]:
#        real_word = True
#if real_word == False:
#    print("Your guess, " + guess + ", is not a word.\nPlease try again:")
#else:
#    (rest of code)
word = "hello" # This line will be removed once the list of words is incorporated.
playing = True # The variable "playing" is set to "True".
print("Welcome to Wordle!") # When the user begins playing, they are greeted by the program.
while playing == True: # This only becomes false, breaking the loop, if the user inputs "no" to the question of if they want to play again.
    print("Guess a five-letter word:")
    for i in range(6): # Wordle allows a maximum of 6 guesses, so the loop runs up to 6 times.
        while True: # This section is for dealing with user-input errors.
            guess = input()
            if len(guess) == 5 and guess.isalpha(): # This is the correct format. The "real word" code would probably go somewhere in here.
                break # This breaks the while loop. If there's something wrong with the guess, the loop repeats, and the wrong-format guess isn't counted as one of the 6 attempts.
            elif guess.isalpha() == False: # This is if non-letter characters (including spaces and punctuation) are included.
                print("Make sure your word only contains letters!\nPlease try again:")
            elif len(guess) != 5: # This is if the length of the string is anything other than 5.
                print("Make sure your word is five letters long!\nPlease try again:")
            else: # This case should never happen, but just in case, I've added a general statement.
                print("Incorrect format.\nPlease try again:")
        guess = guess.lower() # This makes case irrelevant.
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
    print("Would you like to play again?\nAnswer yes or no:") # The user is asked if they'd like to play again.
    while True:
        answer = input()
        if answer.lower() == "yes": # Case is irrelevant for both "yes" and "no".
            break # If the answer is "yes", the while loop breaks without changing the state of "playing", so the main while loop (the one that contains the body of the game) repeats.
        elif answer.lower() == "no":
            playing = False # If the answer is "no", "playing" is set to "False". Then both while loops break, so the program moves on.
            break
        else:
            print("Please answer yes or no:") # If neither "yes" nor "no" is given, the while loop continues, and the user is prompted again to answer "yes" or "no".
print("Goodbye!") # After the user decides to stop playing, they are given a farewell.