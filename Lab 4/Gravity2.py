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
    inp = "" #Variable of the string of the decyphered text
    for alph in text: #Loops through the input of the user
        if alph.isalpha(): #Using ASCII format, checks to see if the character is alphabetical
            if alph.islower(): #If the ASCII letter is lowercase
                inp += chr((ord(alph)-shift-97) % 26 + 97) #Lowercase letters on ASCII code begin at 97, ord checks the code and we compute it to 0 where it will be modulated
            if alph.isupper(): #If the ASCII letter is uppercase
                inp += chr((ord(alph)-shift-65) % 26 + 65) #Uppercase letters on ASCII code begin at 65, ord checks the code and we compute it to 0 where it will be modulated
        else: 
            inp += alph #Adds a space where necessary
    return inp

def decrypt_atbash(text: str) -> str:
    inp = "" #Variable of the string of the decyphered text
    for alph in text: #Loops through the input of the user
        if alph.isalpha(): #Using ASCII format, checks to see if the character is alphabetical
            if alph.islower(): #If the ASCII letter is lowercase
                inp += chr((25-(ord(alph)-97) % 26) + 97) #Lowercase letters on ASCII code begin at 97, ord checks the code and we compute it to its inverse where it will be modulated
            if alph.isupper(): #If the ASCII letter is uppercase
                inp += chr((25-(ord(alph)-65) % 26) + 65) #Uppercase letters on ASCII code begin at 65, ord checks the code and we compute it to its inverse where it will be modulated
        else:
            inp += alph #Adds a space where necessary
    return inp

def main() -> None:
    shift = 3 #The shift to use
    text = input("Enter a text to decipher: ")
    caesar = decrypt_caesar(text, shift) #Final run through of arguments for the caesar function
    atbsh = decrypt_atbash(text) #Final run through of arguments for the atbash function
    print("caesar: ",caesar)
    print("atbash: ",atbsh)

if __name__ == "__main__":
    main()