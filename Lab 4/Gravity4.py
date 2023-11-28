#Help Dipper and Mabel discover the secret messages by writing a program that will help you uncover the mysteries of a cipher that combines all three methods that you know:

#A1Z26 cipher
#Atbash cipher
#Caesar cipher

#A combined cipher is a mix of two or more ciphers seen in the show. The first time such a cipher has been used is at the end of "Gideon Rises." It's solved by converting to letters using the A1Z26 cipher, then flipping the letters with the Atbash cipher, and finally by using the Caesar cipher (source).

#Here's the message that Dipper and Mabel needed to decipher in that episode:

#5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19


#First, they applied the A1Z26 cipher to the message to get the following message:

#ESWFUP RIF DPS VLOJTSYS


#Not very readable. Next, they applied the Atbash cipher to it to get the following message:

#VHDUFK IRU WKH EOLQGHBH


#Finally, they applied the Caesar cipher to it... and, yoohoo! The message is:

#SEARCH FOR THE BLINDEYE


#You will write a program that tries to decipher the message using all three methods and their combinations.

#Your program doesn't need to choose the best method. It just needs to try them all. Don't worry, it will be easy for Dipper and Mabel to figure out which method is correct. Likely, there will be only one decrypted message that makes sense.
#What to do

#You have already implemented all user-defined functions that you need. Now, your goal is to update your main() function.

#You can not add any new user-defined functions.

#Your program must try to decipher a given message with the following ciphers and combinations:

#Caesar cipher with shift 3
#Atbash cipher
#Combined: first apply Caesar cipher with shift 3, then Atbash cipher
#Combined: first apply Atbash cipher, then Caesar cipher with shift 3
#A1Z26 cipher
#Combined: first apply A1Z26 cipher, then Caesar cipher with shift 3
#Combined: first apply A1Z26 cipher, then Atbash cipher
#Combined: first apply A1Z26 cipher, then Atbash cipher, then Caesar cipher with shift 3
#Combined: first apply A1Z26 cipher, then Caesar cipher with shift 3, then Atbash cipher

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
    combined1 = decrypt_atbash(decrypt_caesar(text,shift))
    combined2 = decrypt_caesar(decrypt_atbash(text),shift)
    combined3 = decrypt_caesar(decrypt_a1z26(text),shift)
    combined4 = decrypt_atbash(decrypt_a1z26(text))
    combined5 = decrypt_caesar(decrypt_atbash(decrypt_a1z26(text)),shift)
    combined6 = decrypt_atbash(decrypt_caesar(decrypt_a1z26(text),shift))
    print("caesar: ",caesar)
    print("atbash: ",atbsh)
    print("a1726: ",a1726)
    print("combined 1: ", combined1)
    print("combined 2: ", combined2)
    print("combined 3: ", combined3)
    print("combined 4: ", combined4)
    print("combined 5: ", combined5)
    print("combined 6: ", combined6)
if __name__ == "__main__":
    main()
