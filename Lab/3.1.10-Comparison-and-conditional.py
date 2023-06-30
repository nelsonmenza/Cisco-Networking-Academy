'''Write a program that utilizes the concept of conditional execution, takes a string as input, and:

prints the sentence "Yes - Spathiphyllum is the best 
plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.'''

# Prompt the user to enter a word and store it in the variable 'plant'
plant = input("Enter a word: ")

# Check if the inputted word is exactly "Spathiphyllum" (upper-case)
if plant == "Spathiphyllum":
    # Print the corresponding message if the condition is true
    print("Yes - Spathiphyllum is the best plant ever!")

# Check if the inputted word is exactly "spathiphyllum" (lower-case)
elif plant == "spathiphyllum":
    # Print the corresponding message if the condition is true
    print("No, I want a big Spathiphyllum!")

else:  # If none of the above conditions are true
    # Print the default message with the inputted word substituted
    print(f"Spathiphyllum! Not {plant}!")
