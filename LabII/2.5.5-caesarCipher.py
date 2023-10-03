def main():
    return text_encrypt()


def text_encrypt():
    text = input("Enter your text: ")
    encrypt_text = ""
    while True:
        shift = int(
            input("Enter a number between 1 to 25 to encrypt your text: "))
        if shift > 0 and shift < 26:
            break
        else:
            print("Enter a valid number.")
    for char in text:
        if ord(char) > 64 and ord(char) < 91:
            new_char = ord(char)+shift
            if new_char > 90:
                new_char = (new_char-90)+64

            chr(new_char)
            encrypt_text += chr(new_char)

        elif ord(char) > 96 and ord(char) < 123:
            new_char = ord(char)+shift
            if new_char > 122:
                new_char = (new_char-122)+96
            encrypt_text += chr(new_char)
        else:
            encrypt_text += char
    return encrypt_text


if __name__ == "__main__":
    print(main())
