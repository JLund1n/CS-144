
def decrypt_caesar(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main() -> None:
    text = input("Enter a text to decipher: ")
    shift = 3
    deciphered_text = decrypt_caesar(text, shift)
    print("Deciphered text:", deciphered_text)

if __name__ == "__main__":
    main()