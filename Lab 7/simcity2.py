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

def main() -> None:
    """
    Main program.
    """
    grid = create_grid('data_0.txt')
    print("Sim City Land Values:")
    display_grid(grid)
if __name__ == "__main__":
    main()
