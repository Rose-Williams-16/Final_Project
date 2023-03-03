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

#R represents Raisa's feedback in comments
 
#R:I don't know if this will help, but WordNet is a database that you could look into but I'm not sure how to use it here
#R:here's a website that lists other word databases you could use so that you may not need to list out a bunch of words the 
#program needs to randomly select from
#You mentioned that this list would be used to verify if it's a valid word or not and I think that a databse would be able
#to help with that - but ask Professor Acacia Ackles to make sure this is an ok idea
#if you are planning on doing this, I would recommend using the pandas package because that's good for working with large databases like
#this one
#e.g. in line 7 you can write word_list = pd.read_csv("wordnet_database") 

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

#R: your comments are clear
#R: you said that you wanted to convert it to a format that includes more functions - can you explain what you mean by that?
#the code is working pretty well without functions - other than the word database and the user input check, I think this
#project is doing well and you could just use this as it is
#I guess one thing you could do is define a function that takes in input from the word database and set that function to a variable name
#e.g. def word():
#      the code you have written in lines 7 and 8
#then in line 17 you write word = word()
#you could also have another function that checks the user input that would include the code from lines 9-14 
# and then put all the code from 27-87 under a function then call the function at the end of the check function but I'm not sure 
#if that would work 
#you could also just indent/tab the code from lines 27-87 and put it as a huge chunk of code together after line 16