#!/usr/bin/python3
"""Your program must:
-ask the user to enter a word;
-use user_word = user_word.upper() to convert the word entered by the user to upper case;
-use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
-print the uneaten letters to the screen, each one of them on a separate line."""

user_word = input("Enter a word: ")  # Prompt the user to enter a word
user_word = user_word.upper()  # Convert the word to uppercase
vowels = "AEIOU"  # Sequence of vowels

# Iterate over each letter in the user's word
for letter in user_word:
    if letter in vowels:  # Check if the current letter is a vowel
        continue  # Skip the vowel letters and continue to the next iteration
    else:
        print(letter)  # Print the uneaten letters (non-vowels) on separate lines
