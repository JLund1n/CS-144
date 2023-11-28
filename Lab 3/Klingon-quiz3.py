#Read data from the same file, klingon-english.txt, which you used in the previous versions
#Ask the user to choose a Klingon consonant they want to practice with. Ask again if the user’s answer is not a valid Klingon consonant, until the user enters a valid consonant.
#Find a Klingon word that starts with the chosen consonant (the text file contains only one word that starts with any given consonant).
#Ask the user to translate the chosen word into Klingon
#Print Correct if the user’s answer is correct
#Print Sorry, you’re wrong! The correct answer is ... if the user’s answer is wrong
#You will add in this version:
#Give the user 3 attempts to guess the correct answer. Use an iterative statement to implement this feature. 
#If the answer is incorrect in the first attempt, show a hint: the first and last characters of the correct Klingon word. 
#When showing a hint, replace all other characters with a star (*)
#If the answer is still incorrect in the second attempt, show the same hint once again.
#You will refactor in this version:
#Print Sorry, you’re wrong! The correct answer is ... if all three user’s answers are wrong

class klingon(): #Initializes objects
    def __init__(self,translation):
        self.translation = translation
    def logic(self): #Beginning of logic
        file = open('klingon-english.txt',"r") #Opens file for reading
        consonants = ["b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y", "'"
] #Consonants Array
        if self.translation not in consonants: #loops through until a sufficient consonant is choosen
            x = False
            while x == False:
                test = input("Not a consonant\n")
                if test in consonants:
                    self.translation = test
                    break
        tries = 3
        for n in file.readlines(): #Loops through for consonant
            if self.translation in n[0] or self.translation in (n[0] + n[1]):
                split = n.split('|') #Splits translation up
                inp2 = input("Translate "+split[1]) #Asks for user input
                tran = split[0]
                if inp2 == split[0]: #General if else statement for try 1
                    print("Correct")
                if inp2 != split[0]:
                    print("Sorry, you’re wrong! have 2 more tries")
                    tries = 2 
                if tries == 2: #Hint sequence
                   print("your hint is",tran[0],"*"*(len(tran)-2),tran[len(tran)-1]) #Gives you a hint
                   inp2 = input("Second attempt\n")
                   if inp2 == split[0]: #General if else statement for try 2
                       print("correct")
                   if inp2 != split[0]: #General if else statement for try 3
                       inp2 = input("last attempt\n") 
                       if inp2 == split[0]:
                           print("correct")
                       if inp2 != split[0]:
                           print("Sorry, you’re wrong! The correct answer is",split[0])
                    
                   

inp = input("Klingon consonant to practice\n")
fin = klingon(inp)
fin.logic()
