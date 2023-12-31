#!/usr/bin/python3
'''write a program that uses a for loop to "count mississippily" to five. 
Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"'''
import time

# Use a for loop to count "Mississippi" up to five
for i in range(5):
    i += 1  # Increment i by 1 (starts from 0, so add 1 to match the counting)
    print(i, "Mississippi")
    time.sleep(1)  # Pause for 1 second between each count

print("Ready or not, here I come!")  # Print the final message
