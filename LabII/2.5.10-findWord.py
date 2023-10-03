"""Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the second string?"""

word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

count = 0

lst_word = [char for char in word]
for i in lst_word:
    if i in strn:
        count += 1

if count == len(word):
    print("Yes")
else:
    print("No")
