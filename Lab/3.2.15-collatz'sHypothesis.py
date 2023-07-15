c0 = int(input("Enter a number: "))  # Read a number from the user
step = 0  # Initialize the step count to 0

while c0 != 1:
    if c0 % 2 == 0:  # Check if the number is even
        step += 1  # Increment the step count by 1
        c0 = c0 // 2  # Update the value of c0 by dividing it by 2
        print(c0, end=", ")  # Print the updated value of c0
    else:
        step += 1  # Increment the step count by 1
        c0 = 3 * c0 + 1  # Update the value of c0 according to the formulak
        print(c0, end=", ")  # Print the updated value of c0

print("Steps:", step)  # Print the total number of steps taken
