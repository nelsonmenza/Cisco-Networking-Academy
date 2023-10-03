"""Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.
"""


def palindrome():
    text = input("Enter your text: ")
    reversed_text = text[::-1]
    text, reversed_text = remove_space(text, reversed_text)
    if text == reversed_text:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


def remove_space(text, reversed_text):
    new_text = ""
    new_reversed_text = ""
    for x in text:
        if x != " ":
            new_text += x

    for i in reversed_text:
        if i != " ":
            new_reversed_text += i

    return new_text.lower(), new_reversed_text.lower()


palindrome()
