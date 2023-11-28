#The Caesar cipher is a shifting cipher. Each letter in the message is shifted by a certain number of positions in the alphabet. 

#For example, to encrypt the message "AY" using Caesar cipher with shift 3, you would need to shift each letter by 3 positions:

#Letter A is shifted 3 positions to the right, so it becomes D.
#Letter Y is shifted 3 positions to the right, so it becomes B.

#The resulting message would be "DB".

#So, to decrypt the message, you would need to shift each letter by 3 positions in the opposite direction.

#In this lab, you will implement ONLY decryption, don't worry about encrypting messages. You will implement and test a function that will decrypt an encrypted message.  The messages used in the test cases have been encrypted using Caesar cipher with shift 3 but your function should work with ANY shift, not only 3.   

#Your function should correctly decrypt both upper-case and lower-case letters and keep all other characters (whitespace, punctuation, etc.) intact.





#Implement the decrypt_caesar function that would decrypt a given message with the Caesar cipher.

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

def main() -> None:
    shift = 3 #The shift to use
    text = input("Enter a text to decipher: ")
    caesar = decrypt_caesar(text, shift) #Final run through of arguments for the caesar function
    print("caesar: ",caesar)

if __name__ == "__main__":
    main()

