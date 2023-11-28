MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]: 
    """
    Loads a map from a file as a grid (list of lists)
    """
    with open(map_file, 'r') as file: #Reads the map file
        grid = [list(line.strip()) for line in file] #Nested loop which strips the empty spaces in the file and lists each stripped line
    return grid #returns the final grid from the line above


def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    for i, row in enumerate(grid): #Loops over the rows of the the enumerated grid
        for j, cell in enumerate(row):#the enumerated grid gave an output of two positions (cells) which are then looped over again
            if cell == 'S': #Checks for the starting position
                return [i, j] #Returns the starting position

def get_command() -> str:
    """
    Gets a command from the user.
    """
    return input('> ').lower() #Simply grabs a command from the user and converts to lower case

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    # A simple dictionary that maps symbols to Unicode characters
    symbols = {
        '-': '\U0001F9F1',
        '*': '\U0001F7E2',
        'S': '\U0001F3E0',
        'F': '\U0001F3FA',
        '@': '\U0001F9DD',
    }
    
    # Copies the grid to avoid modifying the original
    grid_copy = [row.copy() for row in grid]
    
    # Loop to replace symbols with new unicode
    for i in range(len(grid_copy)): #Loops over the copy grip
        for j in range(len(grid_copy[i])): #For each cell in the copy grip that becomes looped over
            if grid_copy[i][j] in symbols: #Checks to see if that position is in the symbol dictionary
                grid_copy[i][j] = symbols[grid_copy[i][j]] #Changes to unicode character from the dictionary above
    
    # Add the player to the grid
    player_row, player_col = player_position #Takes the row and column of the player position (S)
    grid_copy[player_row][player_col] = symbols['@'] #Once a move has been made the new player position is generated with an (@)
    
    # Display the grid
    for row in grid_copy: #Loops over the copy grid
        print(' '.join(row)) #Joins each row (cell) to complete the grid
    

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    return [len(grid), len(grid[0])] #Grabs the lens of the row and column

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    rows, cols = get_grid_size(grid) #Grabs the columns and rows of the grid
    return 0 <= position[0] < rows and 0 <= position[1] < cols #Checks to see if the player is within the bounds of the row and columns


def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    directions = [] #Empty map of the directions
    moves = {'north': [-1, 0], 'south': [1, 0], 'west': [0, -1], 'east': [0, 1]} #List of the available moves to be made with their row,col modifiers
    for move, direction in moves.items():
        new_position = [player_position[0] + direction[0], player_position[1] + direction[1]] #Defines the new position by adding the corresponding row and col values
        if is_inside_grid(grid, new_position) and grid[new_position[0]][new_position[1]] != '-': #Checks to see if the player will be within the bounds of the map
            directions.append(move) #Appends the available directions to the empty map
    return directions

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    moves = {'north': [-1, 0], 'south': [1, 0], 'west': [0, -1], 'east': [0, 1]}
    new_position = [player_position[0] + moves[direction][0], player_position[1] + moves[direction][1]]#Defines the new position by adding the corresponding row and col values
    if is_inside_grid(grid, new_position) and grid[new_position[0]][new_position[1]] != '-':#Checks to see if the player will be within the bounds of the map
        player_position[0], player_position[1] = new_position #Generates the new position of the player
        return True
    else:
        return False

def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    player_row, player_col = player_position #Gets the position of the player
    return grid[player_row][player_col] == 'F' #If the player reaches the finish position "F" then return this value

def display_help() -> None:
    """
    Displays a list of commands.
    """
    with open('help.txt', 'r') as f:
        help_text = f.read()
    print(help_text)
    #To implement the display_help() function, we can simply read the contents of the help.txt file and print them to the console.

def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE) #Gets the grid of the map
    player_position = find_start(grid) #Gets the player position
    
    while True: #If true from move function
        display_map(grid, player_position) #Displays the map
        print("You can go", ", ".join(look_around(grid, player_position)))#Displays the available positions

        command = get_command()#Gets a command from the user

        if command.startswith("go "): #Checks to see if the command is valid
            direction = command.split()[1]#Grabs the direction of the command
            if move(direction, player_position, grid):#If the direction is valid
                print(f"You moved {direction}.") #Tell the user the move worked
            else:
                print("There is no way there.")#The move was either out of bounds or not on the path
            if check_finish(grid, player_position):#The player reached the (F)
                print('Congratulations! You have reached the exit!')
                break
        elif command == "show map": #If the player would like to see the map
            display_map(grid, player_position)
        elif command == "escape":#If the player would like to exit the game
            break
        elif command == "help":#If the player needs help
            display_help()
        else:
            print("Invalid command. Try again.")

if __name__ == '__main__':
    main()