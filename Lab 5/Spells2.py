#In this version, you will add quite a few user-defined functions to your typing trainer:
#In this version, your program will:
#Display header
#Display instructions
#Get user input
#Display feedback
#Instructions: instructions.txt
#What to do
#Your program should do the following:
#1. Read spells from the text file (spells.txt)
#2. Display the header as follows:    ############################################################ 
#Harry Potter Typing Trainer
############################################################
#(there are 60 # characters in each line)
#3. Display the instructions (read the instructions from instructions.txt)
#4. Choose a random spell
#5. Get the user’s input and compare it with the chosen spell
#6. If the user typed the spell correctly, display
#Correct!
#Otherwise, display:
#Incorrect!
#The spell was: chosen_spell
#(replace chosen_spell with the randomly chosen spell)
#7.In this version, we don’t care about the case of the user input (in other words, CONFUNDO or CoNfUnDo would be the same as confundo).
#You need to implement the display_header and display_instructions, get_user_input, and display_feedback functions.
#Use the following template. All functions defined in the template must be present 
#and implemented in your code. You cannot change the header of the functions given in the template or omit these functions. 
#You may add extra functions if needed. You cannot change the main function in this version.





def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    read = open(filename,'r') #Opens file
    return(read.readlines()) #Reads the lines in the file   

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    import random #Random module
    return((random.choice(spells)).lower()) #Grabs a random spell and makes it lowercase


def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    header1 = "############################################################\n"
    header2 = "Harry Potter Typing Trainer\n"
    header3 = "############################################################" #3 header lines
    header4 = header1 + header2 + header3 #Adds all of the necessary header lines
    return(print(header4)) #Returns the header

def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    read = open('instructions.txt','r') #Reads the instructions text file
    return(print(read.read())) #Print the instructions

def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    inp = input("Type the following spell: " + spell) #Grabs the user input relative to the spell
    return(inp) #Return the input

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if user_input.strip() == spell.lower().strip(): #Simple if loop to check if the user input matches the spell
        return(print("Correct!"))
    else:
        return(print("Incorrect\nThe spell was:",spell))

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)



if __name__ == '__main__':
    main()
