MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    with open(map_file, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def find_start(grid: list[list[str]]) -> list[int]:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return [i, j]

def get_command() -> str:
    return input('> ').lower()

def display_map(grid: list[list[str]], player_position: list[int]) -> None:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if [i, j] == player_position:
                print('@', end='')
            else:
                print(cell, end='')
        print()

def get_grid_size(grid: list[list[str]]) -> tuple[int, int]:
    return [len(grid), len(grid[0])]

def is_inside_grid(grid: list[list[str]], position: list[int]) -> bool:
    rows, cols = get_grid_size(grid)
    return 0 <= position[0] < rows and 0 <= position[1] < cols

def look_around(grid: list[list[str]], player_position: list[int]) -> list[str]:
    directions = []
    moves = {'north': [-1, 0], 'south': [1, 0], 'west': [0, -1], 'east': [0, 1]}
    for move, direction in moves.items():
        new_position = [player_position[0] + direction[0], player_position[1] + direction[1]]
        if is_inside_grid(grid, new_position) and grid[new_position[0]][new_position[1]] != '-':
            directions.append(move)
    return directions

def move(direction: str, player_position: list[int], grid: list[list[str]]) -> bool:
    moves = {'north': [-1, 0], 'south': [1, 0], 'west': [0, -1], 'east': [0, 1]}
    new_position = [player_position[0] + moves[direction][0], player_position[1] + moves[direction][1]]
    if is_inside_grid(grid, new_position) and grid[new_position[0]][new_position[1]] != '-':
        player_position[0], player_position[1] = new_position
        return True
    else:
        return False

def main():
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)

    while True:
        display_map(grid, player_position)
        print("You can go", ", ".join(look_around(grid, player_position)))

        command = get_command()

        if command.startswith("go "):
            direction = command.split()[1]
            if move(direction, player_position, grid):
                print(f"You moved {direction}.")
            else:
                print("There is no way there.")
        elif command == "show map":
            display_map(grid, player_position)
        elif command == "escape":
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()