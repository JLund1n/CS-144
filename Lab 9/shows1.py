"""
This version of the program:
1. Loads the data from a JSON file
2. Searches for a TV show in the data
3. Prints the name of the show if found
"""

import json

def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    with open(filename,'r') as file:
        data = json.load(file)
    return(data)


def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    for show_name, item in shows.items():
        if query.lower() in show_name.lower():
            return show_name
    return None

def main():
    """
    Main function 
    """
    shows = load_json("tvshows.json")
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)
    if show_name:
        print(f"Found: {show_name}")
    else:
        print("Can't find this TV show in the Top 100!")

if __name__ == '__main__':
    main()