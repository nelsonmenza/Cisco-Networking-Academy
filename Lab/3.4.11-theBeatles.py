"""Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list."""

beatles = []  # Step 1: Create an empty list named beatles
print("Step 1:", beatles)

# Step 2: Add members of the band using the append() method
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in beatles:  # Step 3: Prompt the user to add more members using a loop and the append() method
    if len(beatles) != 5:
        beatles.append(input("Enter a band member: "))

print("Step 3:", beatles)

del beatles[-1]  # Step 4: Remove the last two members using the del keyword
del beatles[-1]
print("Step 4:", beatles)

# Step 5: Add Ringo Starr to the beginning of the list using the insert() method
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Print the length of the list using the len() function
print("The Fab", len(beatles))
