"""
Your task is to write your own function, 
which behaves almost exactly like the original split() method
"""


def mysplit(strng):
    new_strng = ""
    lst = []
    for chr in strng:
        if chr != " ":
            new_strng += chr
        else:
            if new_strng != "":
                lst.append(new_strng)
                new_strng = ""
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
