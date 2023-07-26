#!/usr/bin/python3
'''Task is to help the magician complete the code in the editor in such a way so that the code:

will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number picked by the magician. 
If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. 
If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: 
"Well done, muggle! You are free now."'''
secret_number = 777  # Define the secret number

# Print the welcome message and instructions
print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = 0  # Initialize the number variable to 0

# Loop until the user guesses the secret number
while number != secret_number:
    # Prompt the user to choose a number
    number = int(input("Choose a number: "))
    # Display a message indicating they are stuck in the loop
    print("Ha ha! You're stuck in my loop!")

# Display a message indicating they have guessed the secret number
print("Well done, muggle! You are free now.")
