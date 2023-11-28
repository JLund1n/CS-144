#Have you ever played Yahtzee? It’s a board game that is played by two players. 
#The players take turns rolling five 6-sided dice, and the player with the highest score wins.
#Now might be a good time to review the game rules: Yahtzee Game Rules.
#In the first version, you will implement user-defined functions for the Upper Section of Yahtzee.
#Your main function will do the following:
#1. Display the random roll by calling the make_roll function. The make_roll function returns a tuple of 5 random numbers between 1 and 6 (both endpoints inclusive).  Let’s assume that the make_roll function returns the random roll (2, 1, 5, 1, 5), the following message will be displayed by the main function:
#Rolling the dice... (2, 1, 5, 1, 5)

#2. Fill the upper section of Yahtzee by calling the fill_upper_section function. The fill_upper_section function takes the random roll as a parameter and returns a list.  In the resulting list, each element will represent the sum of all occurrences of a specific number that appears in the random roll.  If there are two ones in the random roll, the first element of the list should be 2. If there's only one two, the second element of the list should be 2. If a number doesn't appear in the roll, its corresponding element should be 0. 

#For example, if the random roll was (2, 1, 5, 1, 5), the list returned by this function will look like this:
#[2, 2, 0, 0, 10, 0]
#It means that the sum of all ones is 2 (there are two ones), the sum of all twos is 2 (there is a single two), the sum of all threes is 0 (there are no threes), etc. 

#The fill_upper_section function will call the sum_of_given_number function for each number from 1 to 6 to compute and return the sum of all occurrences of that number. 
#Unlike real Yahtzee, in our simplified version, the player rolls only once to fill out the entire upper section.

#3. Display the upper section as follows by calling the display_upper_section function:
#Aces: 2
#Twos: 2
#Threes: 0
#Fours: 0
#Fives: 10
#Sixes: 0


#Use the following template. All functions defined in the template must be present and implemented in your code (you may not omit functions). You may add extra functions if needed. 


import random
def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    roll = ()
    n = 1
    while n < 6:
        rand = random.randrange(1,7)
        roll = roll + (rand,)
        n = n + 1
    print("Rolling the dice...", roll)
    return(roll)


def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    Example: sum_of_given_number((2,6,2,6,1), 6) = 12
    """
    total = 0
    for n in roll:
        if int(n) == int(number):
            total = total + int(number)
    return(total)


def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    upper_section = ()
    n = 1
    while n < 7:
        upper_section = upper_section + (sum_of_given_number(roll,n),)
        n = n + 1
    return(upper_section)

def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    print("Upper Section:")
    t = 0
    for n in names:
        print(n+":", upper_section_scores[t])
        t = t + 1
    
def main():
    """
    Main function.
    """
    fillupper = fill_upper_section(make_roll())
    display_upper_section(fillupper)

if __name__ == "__main__":
    main()


