#In this version, you will add a game loop (to play multiple times) and implement a simple scoring system:
#Each correct answer should add 10 points to the score
#Each incorrect answer should subtract 5 points from the score
#What to do
#In addition to the functions implemented in Version 1 and Version 2, implement the following:
#1. Implement the play_again function that would ask the user if they want to play again.
#2. Add a game loop to your main function. After each attempt, your program should call the play_again function:
#	a) If the user wants to continue, show another spell
#	b) Otherwise, print the final score and quit.
#3. Add scoring functionality to your main() function:
#	a) For each correct answer, add 10 points to the score and print the score
#	b) For each incorrect answer, subtract 5 points from the score and print the score
#The total score can be negative.


# All functions implemented in Version 2 code should be placed here

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
    global score #Global score variable
    score = 0
    if user_input.strip() == spell.lower().strip(): #Simple if loop to check if the userinput matches the spell and then adds points based on result
        score = score + 10
        return(print("Correct!"))
    else:
        score = score - 5
        return(print("Incorrect\nThe spell was:",spell))

def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """
    inp = input("Would you like to play again (Y/N):") #Grabs user input of yes or no
    if inp == 'Y' or inp == 'y': #If loop to see if the user wants to play again
        return(True)
    else:
        return(False)

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    finalscore = 0 #final score based on Global score
    while True: #Loop relative to the bool instantiated by the play_again() function
        spell = get_random_spell(spells) #Grabs a new spell
        user_input = get_user_input(spell) #Checks the user input relative to the spell
        display_feedback(spell, user_input) #Gives feedback based on the result of the userinput in contrast with the spell
        if score == 10: #Final score calculation
            finalscore = finalscore + 10
        else:
            finalscore = finalscore - 5
        if play_again() == False:
            print(finalscore)
            break
if __name__ == '__main__':
    main()