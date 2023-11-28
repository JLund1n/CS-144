MAP_FILE = 'cave_map.txt'

def load_map (map_file: str) -> list[list[str]]:
    dmap = [] #Initializes an empty map to be configured                           
    with open (map_file) as m: #Opens the map file
        for line in m: #Loops through each line of the map      
            lst = list(line.strip()) #Strips each line of an empty space                           
            dmap.append (lst) #Appends the line to the empty map                                    
    return dmap #Returns the finished map
    
def find_start (grid: list[list[str]]) -> list[int, int]:
    for i in range (len (grid)): #Loops through the rows of the grid                             
        for j in range (len (grid [0])): #Loops through the columns of the grid                  
            if grid [i][j] == 'S': #If the row and column correspond to the start point (S)
                return [i, j] #Returns to coords of the start                                  

def get_command () -> str:
    return input ("Command: ") #Gets a command from the user                              
def main ():
    grid = load_map (MAP_FILE) #Loads the map file
    print (grid) #Prints the map
    print (find_start (grid)) #Prints the start location of the map
    while True:                                                 
        cmd = get_command () 
        if cmd == 'escape': #If the command is as such exit the game
            return 
        else:
            print ('I do not understand') #Any other command print this

if __name__ == "__main__":
    main ()