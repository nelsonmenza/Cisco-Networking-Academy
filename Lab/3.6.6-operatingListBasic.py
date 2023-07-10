# Write a program to remove number repetitions from a list and create a new list with unique elements only.

# Input list with number repetitions
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Create an empty list to store unique elements
lst = []

# Iterate over each element in the original list
for i in my_list:
    if i in lst:  # Check if the element already exists in the new list
        continue  # If it does, skip adding it to avoid repetitions
    else:
        lst.append(i)  # If it doesn't, add it to the new list

# Update the original list with the new list containing unique elements
my_list = lst

# Print the list with unique elements only
print("The list with unique elements only:")
print(my_list)
