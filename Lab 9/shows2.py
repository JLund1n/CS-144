import json

"""
New features in this version:
* Formatting the show details
"""

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

def get_show_data_by_name(show_name: str, shows: dict) -> dict:
    """
    Return the data for a show based on its name
    """
    for name, data in shows.items():
        if show_name.lower() == name.lower():
            return data
    return None
def format_show_details(show: dict) -> str:
    """
    Format the show details
    """
    show_name = show.get('name', 'Unknown')
    premiere_year = show.get('premiered', '?')[:4]
    end_year = show.get('ended', '?')[:4] if show.get('status') == 'Ended' else '?'
    genres = ', '.join(show.get('genres', ['Unknown']))

    formatted_details = f"{show_name} ({premiere_year} - {end_year}, {genres})"
    return formatted_details

def main():
    shows_filename = 'tvshows.json' 
    shows = load_json(shows_filename)

    while True:
        user_input = input("Enter a TV show name (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break

        found_show = find_show(user_input, shows)

        if found_show:
            show_data = get_show_data_by_name(found_show, shows)
            formatted_details = format_show_details(show_data)
            print(f"Found: {formatted_details}")
        else:
            print("Can't find this TV show in the Top 100!")

if __name__ == '__main__':
    main()