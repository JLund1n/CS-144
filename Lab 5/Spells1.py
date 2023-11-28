#In this version, you will read the list of spells from a file and display a random spell. It is your first step in the implementation of a typing trainer.
#Remember: you must use user-defined functions to implement this program.
#Text file: spells.txt
#What to do
#Implement the read_spells and get_random_spell functions.
#Import the random module and use it appropriately to  generate the random spell.
#The random spell should always be displayed in all lowercase letters.
#Use the following template. All functions defined in the template must be present and implemented in your code. 
#You cannot change the header of the functions given in the template or omit these functions. 
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


def main() -> None:
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)

if __name__ == "__main__":
    main()

