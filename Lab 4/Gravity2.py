#The mysteries of Gravity Falls must be discovered.

#Help Dipper and Mabel discover the secret messages by writing a program that will help you uncover the mysteries of ciphers!

#Now, you will add one more function to decrypt the message, and your program will provide two potential solutions (one with t#he Caesar cipher and one with the Atbash cipher).

#Dipper and Mabel will choose the one that works best.

#Atbash cipher reverses the alphabet.

#For example:

#Letter A is the first letter in the alphabet, so it will be replaced with the last letter, which is Z.
#Letter D is the 4th letter in the alphabet, so it will be replaced with the 4th letter from the end, which is W.

#Your program should correctly decrypt both upper-case and lower-case letters and keep all other characters (whitespace, punctuation, etc.) intact.
#What to do

#In addition to the decrypt_caesar function that you already have, implement the decrypt_atbash function that would decrypt a given message with the Atbash cipher.

#Keep your decrypt_caesar function as is.
#Implement the decrypt_atbash  function that would decrypt a given message with the Atbash cipher
#Alter your main function so that it  now calls both  decrypt_caesar and decrypt_atbash functions and print the outputs returned by the functions.


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

def main() -> None:
    shift = 3
    text = input("Enter a text to decipher: ")
    caesar = decrypt_caesar(text, shift)
    atbsh = decrypt_atbash(text)
    print("caesar: ",caesar)
    print("atbash: ",atbsh)

if __name__ == "__main__":
    main()