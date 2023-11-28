#Finally, it’s time to make your typing trainer real.
#In this version, your program will time the user's input and calculate the score based on the time and correctness.
#We will use the following formula to estimate the target typing speed:
#Target typing time (TTT) = number of characters * 0.3 seconds
#If the user types the spell correctly, the score is:
#If the user’s typing time is faster or equal to TTT, the score will be 10.
#If the user’s typing time is faster or equal to (TTT * 1.5) but slower than TTT, the score will be 6.
#If the user’s typing time is faster or equal to (TTT * 2) but slower than (TTT * 1.5), the score will be 3.
#If the user’s typing time is slower than (TTT * 2), the score will be 1.
#Otherwise, the score will be -5.
#What to do
#We provided the complete get_user_input function for you. Now, it takes time into account. Carefully study the code of this function and make sure you understand how it works.
#This function return a tuple of two values:
#a) The spell that the user typed
#b) The time it took the user to type the spell (rounded to two digits after the decimal point)
#1. Implement the new get_target_time function to calculate the target time (TTT) using the formula above.
#2. Finally, implement the calculate_points function to calculate the score using the approach above. The score can be a negative number. 
#Use the following template. All functions defined in the template must be present and implemented in your code (you may not omit functions). 
#You cannot change the header of the functions given in the template or omit these functions. 
#You may add extra functions if needed. In this version you will add or modify code in the main function in order to satisfy the requirements of this version. 
#You may add extra functions if needed. 


import time

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


def get_user_input(spell: str) -> (str, float): #Hardcoded userinput function
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    spelllen = len(spell) #Grabs the lenght of the spell
    TTT = round(spelllen * 0.3) #Multiplies the length by 0.3 and uses this number as the time requirement
    return(TTT)

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """
    #If the user’s typing time is faster or equal to TTT, the score will be 10.
    #If the user’s typing time is faster or equal to (TTT * 1.5) but slower than TTT, the score will be 6.
    #If the user’s typing time is faster or equal to (TTT * 2) but slower than (TTT * 1.5), the score will be 3.
    #If the user’s typing time is slower than (TTT * 2), the score will be 1.
    #Otherwise, the score will be -5.
    global score #Global score variable
    score = 0
    if str(user_input).strip() == spell.lower().strip(): #If loop relative to correctness of user input and time taken, grants a score based on such
        if user_time <= get_target_time(spell):
            score = 10
        if user_time <= (get_target_time(spell) * 1.5) and user_time > get_target_time(spell):
            score = 6
        if user_time <= (get_target_time(spell) * 2) and user_time > (get_target_time(spell) * 1.5):
            score = 3
    else:
        score = -5
    return(score)

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if str(user_input).strip() == str(spell).lower().strip(): #If loop to see if what the use typed is correct
        return(print("Correct!"))
    else:
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
        user_input,user_time = get_user_input(spell) #Checks the user input relative to the spell and checks what the time should be
        display_feedback(spell, user_input) #Gives feedback based on the result of the userinput in contrast with the spell
        finalscore = finalscore + calculate_points(spell,user_input,user_time) #Final calculation of points
        if play_again() == False: #Runs the playagain function and checks to see if the user wants to play again
            print(finalscore)
            break

if __name__ == '__main__':
    main()
