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

def decrypt_a1z26(text: str) -> str:
    inp = "" #Variable of the string of the decyphered text
    split = text.split() #Splits the text into num and "-"
    for num in split: #Loops through the split
        hyphen = num.split("-") #Splits the original split at each "-"
        for digit in hyphen: #Loops through the new split
            if digit.isnumeric(): #Checks to see if the digit is an int or space
                inp += chr(int(digit) + 64) #Converts it to uppercase ASCII
        inp += " " #Adds a space where necessary
    return inp

def main() -> None:
    shift = 3 #The shift to use
    text = input("Enter a text to decipher: ")
    caesar = decrypt_caesar(text, shift) #Final run through of arguments for the caesar function
    atbsh = decrypt_atbash(text) #Final run through of arguments for the atbash function
    a1726 = decrypt_a1z26(text) #Final run through of arguments for the a1z26 function
    print("caesar: ",caesar)
    print("atbash: ",atbsh)
    print("a1726: ",a1726)
if __name__ == "__main__":
    main()
