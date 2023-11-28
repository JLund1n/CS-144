import copy
def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file.
    """
    with open(filename, 'r') as file:
        rows = int(file.readline().strip())
        columns = int(file.readline().strip())
        grid = [[int(file.readline().strip()) for _ in range(columns)] for _ in range(rows)]
    return grid

def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values.
    """
    for row in grid:
        print(' '.join(f'{value:>9}' for value in row))

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell in the grid.
    """
    neighbors = []
    # Define the relative positions of the eight possible neighbors
    neighbor_positions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),           (0, 1),
                          (1, -1),  (1, 0),  (1, 1)]
    
    for dr, dc in neighbor_positions:
        r, c = row + dr, col + dc
        # Check if the calculated neighbor position is within the grid bounds
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            neighbors.append(grid[r][c])

    return neighbors

def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid.
    Creates a new grid that is a copy of the original grid.
    Call find_neighbor_values function to find the neighbors of each cell.
    Find the average of their values and round it to the nearest integer.
    Use the average values to fill in the missing values in the new grid.
    Return the new grid. Do NOT modify the original grid!
    """
    new_grid = copy.deepcopy(grid)
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                neighbors = find_neighbor_values(grid, row, col)
                # Filter out zero values from neighbors
                non_zero_neighbors = [value for value in neighbors if value != 0]
                if non_zero_neighbors:
                    average_value = round(sum(non_zero_neighbors) / len(non_zero_neighbors))
                    new_grid[row][col] = average_value
    return new_grid

def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer).
    """
    max_value = max(max(row) for row in grid)
    return max_value

def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer).
    """
    total = sum(sum(row) for row in grid)
    count = sum(len(row) for row in grid)
    average_value = round(total / count)
    return average_value

def main() -> None:
    """
    Main program.
    """
    grid = create_grid('data_3.txt')
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")

if __name__ == "__main__":
    main()
