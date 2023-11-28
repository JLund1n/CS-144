# Import the 'copy' module which provides the 'deepcopy' function, used to create a complete copy of a data structure.
import copy

# Define a function to create a grid of land values from a file.
def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file.
    """
    # Open the file with the given filename in 'read' mode.
    with open(filename, 'r') as file:
        # Read the first line, strip any whitespace and newline characters, and convert to an integer.
        rows = int(file.readline().strip())
        # Do the same for the second line to get the number of columns.
        columns = int(file.readline().strip())
        # Use a list comprehension to create a list of lists (a grid) from the file.
        grid = [[int(file.readline().strip()) for _ in range(columns)] for _ in range(rows)]
    # Return the created grid.
    return grid

# Define a function to display the grid of land values.
def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values.
    """
    # Iterate over each row in the grid.
    for row in grid:
        # Print the row as a string where each value is formatted to be right-justified within 9 spaces.
        print(' '.join(f'{value:>9}' for value in row))

# Define a function to find the neighbor values of a cell in the grid.
def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell in the grid.
    """
    # Initialize an empty list to store neighbor values.
    neighbors = []
    # A list of tuples representing the relative positions of the eight neighbors to a cell.
    neighbor_positions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),           (0, 1),
                          (1, -1),  (1, 0),  (1, 1)]
    
    # Iterate over the neighbor positions.
    for dr, dc in neighbor_positions:
        # Calculate the actual neighbor positions by adding the relative positions to the current cell's position.
        r, c = row + dr, col + dc
        # Check if the neighbor's position is within the bounds of the grid.
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            # If it is within bounds, append the neighbor's value to the list.
            neighbors.append(grid[r][c])

    # Return the list of neighbor values.
    return neighbors

# Define a function to fill in gaps (zeros) in the grid with average values of their neighbors.
def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid.
    """
    # Create a deep copy of the original grid so we do not modify it.
    new_grid = copy.deepcopy(grid)
    
    # Iterate over the rows of the grid.
    for row in range(len(grid)):
        # Iterate over the columns of the row.
        for col in range(len(grid[row])):
            # If the current cell's value is 0, it is a gap that needs to be filled.
            if grid[row][col] == 0:
                # Find the neighbor values of the current cell.
                neighbors = find_neighbor_values(grid, row, col)
                # Filter out zero values from the neighbor values.
                non_zero_neighbors = [value for value in neighbors if value != 0]
                # If there are non-zero neighbors, calculate their average value.
                if non_zero_neighbors:
                    average_value = round(sum(non_zero_neighbors) / len(non_zero_neighbors))
                    # Update the cell in the new grid with the calculated average.
                    new_grid[row][col] = average_value
    # Return the new grid with the gaps filled.
    return new_grid

# Define a function to find the maximum value in the grid.
def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer).
    """
    # Use a generator expression to find the maximum value across all rows.
    max_value = max(max(row) for row in grid)
    # Return the maximum value.
    return max_value

# Define a function to find the average value of the grid.
def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer).
    """
    # Calculate the total sum of all values in the grid.
    total = sum(sum(row) for row in grid)
    # Count the total number of values in the grid.
    count = sum(len(row) for row in grid)
    # Calculate the average and round to the nearest integer.
    average_value = round(total / count)
    # Return the average value.
    return average_value

# Define the main function of the program.
def main() -> None:
    """
    Main program.
    """
    # Create the grid from the file.
    grid = create_grid('data_0.txt')
    # Display the original grid.
    print("Sim City Land Values:")
    display_grid(grid)
    # Fill in the gaps in the grid and display the new grid.
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    # Display statistics about the land values.
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")

# This conditional statement checks if this script is the main program and not being imported by another module.
if __name__ == "__main__":
    # If it is the main program, execute the main function.
    main()
