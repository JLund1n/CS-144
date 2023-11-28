#Create a new file called yahtzee2.py.
#Implement the following user-defined functions and update the main function accordingly:
#num_of_a_kind (this function will generalize both the “3 of a kind” and “4 of a kind”)
#yahtzee
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

def num_of_a_kind(roll: tuple, number: int) -> int:
    """
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    """
    score = 0
    for n in roll:
        if roll.count(n) == number:
            score = score + (n*number)
            break
    return(score)

def yahtzee(roll: tuple) -> int:
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    for n in roll:
        if roll.count(n) == 5:
            return(50)
        else:
            return(0)

def main():
    """
    Main function.
    """
    roll = make_roll()
    fillupper = fill_upper_section(roll)
    display_upper_section(fillupper)
    print("Lower section:")
    print("Three of a kind:", num_of_a_kind(roll,3))
    print("Four of a kind", num_of_a_kind(roll,4))
    print("Yahtzee:", yahtzee(roll))

if __name__ == "__main__":
    main()