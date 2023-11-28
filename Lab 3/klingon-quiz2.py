#Read data from the same file, klingon-english.txt, which you used in Version 1.
#Ask the user to choose a Klingon consonant they want to practice with. Ask again if the user’s answer is not a valid Klingon consonant, until the user enters a valid consonant. 
#Find a Klingon word that starts with the chosen consonant (the text file contains only one word that starts with any given consonant).
#Ask the user to translate the chosen word into Klingon
#Print Correct if the user’s answer is correct
#Print Sorry, you’re wrong! The correct answer is ... if the user’s answer is wrong


#The user is required to enter the consonant in their correct case. Your program does not need to change the case of the consonant entered by the user. 
#The user can enter 2 letter consonants such as ch and gh. Your program should recognize these 2 letter inputs as valid consonants. 
#You must read data from the provided text file, it is absolutely essential in this lab assignment. You can not hardcode the words.

#Here are Klingon consonants: b, ch, D, gh, H, j, l, m, n, p, q, Q, r, S, t, v, w, y, '


class klingon(): #Initializes objects
    def __init__(self,translation): 
        self.translation = translation
    def logic(self): #Beginning of logic 
        file = open('klingon-english.txt',"r") #Opens file for reading
        consonants = ["b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y", "'"
] #Consonants Array
        if self.translation in consonants:
            pass
        else:
            print("not a consonant") #Checks if consonant was asked for
        for n in file.readlines(): #Checks through file for consonant choosen
            if self.translation in n[0] or self.translation in (n[0] + n[1]): #Checks to see if the consonant is in a word
                split = n.split('|') #Splits trabslation
                inp2 = input("Translate "+split[1]) #Asks for user input
                if inp2 == split[0]: #General check
                    print("Correct")
                else:
                    print("Sorry, you’re wrong! The correct answer is",split[0])
        

inp = input("Klingon consonant to practice\n")
fin = klingon(inp)
fin.logic()
