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

def main() -> None:
    shift = 3
    text = input("Enter a text to decipher: ")
    caesar = decrypt_caesar(text, shift)
    print("caesar: ",caesar)

if __name__ == "__main__":
    main()

