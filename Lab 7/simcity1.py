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

def main() -> None:
    """
    Main program.
    """
    grid = create_grid('data_0.txt')
    print("Sim City Land Values:")
    display_grid(grid)

if __name__ == "__main__":
    main()
