'''Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" 
as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and 
the loop should terminate.
Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.'''

while True:
    word_input = input('Enter a word: ')  # Prompt the user to enter a word
    if word_input == 'chupacabra':  # Check if the entered word is 'chupacabra'
        print("You've successfully left the loop.")  # Print the exit message
        break  # Terminate the loop and exit
