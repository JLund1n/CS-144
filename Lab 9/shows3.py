import json

"""
New features in this version:
* Showing all actors in the show and their roles
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

def get_cast_by_id(show_id: int) -> list[dict]:
    """
    Get the cast for a show
    """
    castid = f"cast/{show_id}_cast.json"
    return load_json(castid)

def format_cast(cast: list[dict]) -> str:
    """
    Format the cast
    """
    castid_formatted = ""
    for actor in cast:
        castid_formatted += f'{actor["person"]["name"]} as {actor["character"]["name"]}\n'
    return castid_formatted

def main():
    shows_filename = 'tvshows.json' 
    shows = load_json(shows_filename)

    user_input = input("Enter the name of the show: ")
    selected_show_data = get_show_data_by_name(user_input, shows)

    if selected_show_data:

        print(format_show_details(selected_show_data))

        show_id = selected_show_data['id']
        cast = get_cast_by_id(show_id)
        formatted_cast = format_cast(cast)
        print(f"Cast:\n{formatted_cast}")
    else:
        print(f"Can't find this TV show in the Top 100!")

if __name__ == '__main__':
    main()
