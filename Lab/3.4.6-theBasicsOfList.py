"""There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3)."""

# Initialize the list with numbers 1, 2, 3, 4, and 5
hat_list = [1, 2, 3, 4, 5]

# Prompt the user to enter a number and replace the middle number in the list with it
hat_list[2] = int(input("Enter a number: "))
print("List =", hat_list)  # Print the updated list

del hat_list[-1]  # Remove the last element from the list
print("List =", hat_list)  # Print the updated list

# Print the length of the existing list
print("Length of the existing list =", len(hat_list))
