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

def display_map(grid: list[list[str]], player_position: list[int]) -> None:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if [i, j] == player_position:
                print('@', end='')
            else:
                print(cell, end='')
        print()

def get_grid_size(grid: list[list[str]]) -> tuple[int, int]:
    num_rows = len(grid)
    num_cols = len(grid[0]) if grid else 0
    return [num_rows, num_cols]

def is_inside_grid(grid: list[list[str]], position: list[int]) -> bool:
    num_rows, num_cols = get_grid_size(grid)
    row, col = position
    return 0 <= row < num_rows and 0 <= col < num_cols

def look_around(grid: list[list[str]], player_position: list[int]) -> list[str]:
    allowed_directions = []

    directions = {
        'north': [-1, 0],
        'south': [1, 0],
        'east': [0, 1],
        'west': [0, -1]
    }

    for direction, move in directions.items():
        new_position = [player_position[0] + move[0], player_position[1] + move[1]]
        if is_inside_grid(grid, new_position) and grid[new_position[0]][new_position[1]] in ['*', 'S', 'F']:
            allowed_directions.append(direction)

    return allowed_directions

def get_command() -> str:
    return input('> ')

def main():
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    
    while True:
        display_map(grid, player_position)
        directions = look_around(grid, player_position)
        print(f'You can go {", ".join(directions)}')
        
        command = get_command()
        if command == 'show map':
            display_map(grid, player_position)
        elif command == 'escape':
            break

if __name__ == '__main__':
    main()