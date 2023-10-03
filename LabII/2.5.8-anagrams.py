"""Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result."""
str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

str_1 = str_1.replace(" ", "")
str_2 = str_2.replace(" ", "")
lst_1 = [char1.lower() for char1 in str_1]
lst_2 = [char2.lower() for char2 in str_2]

lst_1.sort()
lst_2.sort()


if lst_1 == lst_2:
    print("Anagrams")
else:
    print("Not Anagrams")
