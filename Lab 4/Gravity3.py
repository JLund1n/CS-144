#Help Dipper and Mabel discover the secret messages by writing a program that will help you uncover the mysteries of ciphers!

#Now, you will add a third function, and your program will provide three potential solutions.

#Dipper and Mabel will examine the output and choose the one that works best.

#A1Z26 cipher is a substitution cipher. It means that it replaces the letter with its number in the alphabet.

#For example:

#Letter A is the first letter in the alphabet, so it will be replaced with 1.
#Letter D is the 4th letter in the alphabet, so it will be replaced with 4.
#Thus, message AD is replaced with 1-4 (a dash is added between each two numbers) in the encrypted message..

#Your program should correctly decrypt the numbers separated by dashes into corresponding uppercase letters.  The dashes in the encrypted message will be removed from the decrypted message. All other characters (whitespace, punctuation, etc.) remain intact.
#Assumptions

#You can safely assume that the original message will never contain any numbers or dashes.
#The A1Z26 cipher is case-insensitive, so you will lose the information about the case of the letters. It's fine.
#What to do

#In addition to the decrypt_caesar and decrypt_atbash functions that you already have, implement the decrypt_a1z26 function that would decrypt  a given message with the A1Z26 cipher.

#Keep your decrypt_caesar and decrypt_atbash functions as is
#Implement the decrypt_a1z26  function that would  decrypt a given message with the A1Z26 cipher
#Alter your main function so that it  now calls decrypt_caesar, decrypt_atbash and decrypt_a1z26 functions and prints the outputs returned by the functions.

def decrypt_caesar(text: str, shift: int) -> str:
    inp = ""
    for alph in text:
        if alph.isalpha():
            if alph.islower():
                inp += chr((ord(alph)-shift-97) % 26 + 97)
            if alph.isupper():
                inp += chr((ord(alph)-shift-65) % 26 + 65)
        else:
            inp += alph
    return inp

def decrypt_atbash(text: str) -> str:
    inp = ""
    for alph in text:
        if alph.isalpha():
            if alph.islower():
                inp += chr((25-(ord(alph)-97) % 26) + 97)
            if alph.isupper():
                inp += chr((25-(ord(alph)-65) % 26) + 65)
        else:
            inp += alph
    return inp

def decrypt_a1z26(text: str) -> str:
    inp = ""
    split = text.split()
    for num in split:
        hyphen = num.split("-")
        for digit in hyphen:
            if digit.isnumeric():
                inp += chr(int(digit) + 64)
        inp += " "
    return inp

def main() -> None:
    shift = 3
    text = input("Enter a text to decipher: ")
    caesar = decrypt_caesar(text, shift)
    atbsh = decrypt_atbash(text)
    a1726 = decrypt_a1z26(text)
    print("caesar: ",caesar)
    print("atbash: ",atbsh)
    print("a1726: ",a1726)
if __name__ == "__main__":
    main()
