#!/usr/bin/python3
"""Your task is to write a function checking whether a number is prime or not.

The function:

is called is_prime;
takes one argument (the value to check)
returns True if the argument is a prime number, and False otherwise.
"""


def is_prime(num):
    # Check if the number is less than 2, as numbers less than 2 are not prime
    if num < 2:
        return False

    # Iterate from 2 to the square root of the number (inclusive)
    for i in range(2, int(num ** 0.5) + 1):
        # Check if the number is divisible by any of the values in the range
        if num % i == 0:
            return False

    # If the number is not divisible by any values in the range, it is prime
    return True


# Print the prime numbers from 1 to 20
for i in range(1, 20):
    # Check if the number (i + 1) is prime using the is_prime() function
    if is_prime(i + 1):
        # Print the prime number followed by a space, using end=" "
        print(i + 1, end=" ")

# Print a newline character to separate the output
print()
