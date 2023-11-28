#Read data from klingon-english.txt. 
#Access the word that is on the third line in the file. 
#Ask the user to translate this word( that is on the third line in the file) into Klingon 
#Print Correct if the user’s answer is correct, or Sorry, you're wrong! The correct answer is De'wI' if the user’s answer is wrong


#You must read data from the provided text file, it is absolutely essential in this lab assignment. 
#Your program will work for the third line of the file only. 
#You can not simply hardcode the word De'wI' or the word computer, it will be considered incorrect. 
#You cannot use the literal computer when prompting the user to translate the word.
#You cannot use the literal De'wI' to display the output when the user’s guess is incorrect. 

#Run your program with python klingon-quiz1.py. Type De'wI' and press Enter. Your program should print:
#Correct!


class klingon(): #Inititalize objects
    def __init__(self,translation): 
        self.translation = translation 
    def logic(self): #Beginning of logic function
        file = open('klingon-english.txt',"r") #Opens the text file
        data = file.readlines()[2] #Reads the line which contains the specified word
        split = data.split('|') #Splits the line into the English and Klingon translation
        if self.translation == str(split[0]): #Compares answer to translation
            print("correct")
        else:
            print("Sorry, you're wrong! The correct answer is De'wI'")
        
file = open('klingon-english.txt',"r")
data = file.readlines()[2]
split = data.split('|')
input = input("Translate "+split[1]+"to klingon\n") #Asks for user input
fin = klingon(input)
fin.logic()
