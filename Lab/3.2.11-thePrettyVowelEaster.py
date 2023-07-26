#!/usr/bin/python3
"""Your program must:

-ask the user to enter a word;
-use user_word = user_word.upper() to convert the word entered by the user to upper case;
-use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it. 
Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, 
and assign it to the word_without_vowels variable."""

# Prompt user to enter a word and convert it to uppercase
user_word = input("Enter a word: ")
user_word = user_word.upper()

# Initialize an empty string to store the word without vowels
word_without_vowel = ""

# Iterate through each letter in the user's word
for letter in user_word:
    # Check if the letter is a vowel (A, E, I, O, U)
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        # If it is a vowel, skip to the next iteration without appending it to the word_without_vowel
        continue
    else:
        # If it is not a vowel, append it to the word_without_vowel
        word_without_vowel = word_without_vowel + letter

# Print the word_without_vowel, which is the user's word without any vowels
print(word_without_vowel)
