# Final_Project
My final project for CMSC 140 -- a Wordle game!

This is similar to the official Wordle game, run by the New York Times.
You will have 6 attempts to guess a 5-letter word.
After each guess, you will be told whether or not each letter of your guess is in the answer and whether or not it is in the correct position.
Your guess must be an actual word, as determined by its presence in the database.  Guesses that are not in the database will not be accepted and will not be counted as one of your 6 attempts.
If you guess the correct word within 6 attempts, you win!
To play, download the Final_Project_Wordle.py and 5_letters.csv files to your device and run the .py file.  Make sure both files are stored in the same folder.
Good luck, and have fun!

More information:
This program uses an external database of 5-letter words, which is in the form of a .csv file.  It also uses the Python modules of Path (from pathlib) to read the file and random to select a random word from the file to be the answer.
The program itself takes in a guess and returns information about each letter in the guess, as specified above.  If the answer is guessed, it informs the user of the number of attempts made.  If the answer is not guessed within 6 attempts, the user is informed of what the answer was.  Either way, the code asks the user if they would like to play another round.