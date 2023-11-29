import json #Imports the json module

"""
New features in this version:
* Searching for an actor/character in the cast
* Showing detailed information about a selected actor/character
"""

def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    with open(filename,'r') as file: #reads the file
        data = json.load(file) #Loads the json file
    return(data) #Returns the loaded json file of tvshows

def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    for show_name, item in shows.items(): #Loops through the loaded json file
        if query.lower() in show_name.lower(): #Checks to see if the user input matches a tvshow
            return show_name #Returns that show
    return None #If no show was found returns None

def find_actor(query: str, cast: list[dict]) -> dict:
    """
    Search for an actor in the cast list
    Return the actor's data if found
    If the actor is not found, return None
    """
    if cast is not None: #If a show and its corresponding data json file was found
        for actor_data in cast: #Loops through the cast data file
            if query.lower() in actor_data['person']['name'].lower(): #Checks to see if the user input matches a cast member
                return actor_data #Returns the cast members data
    return None #If no cast data was found or the user input was invalid returns None

def get_show_data_by_name(show_name: str, shows: dict) -> dict:
    """
    Return the data for a show based on its name
    """
    for name, data in shows.items(): #Loops through the shows
        if show_name.lower() == name.lower(): #Checks to see if the user input matches a tvhshow
            return data #Returns the data of that show
    return None #If the user input is invalid returns None


def format_show_details(show: dict) -> str:
    """
    Format the show name
    """
    show_name = show.get('name', 'Unknown') #Gets the name of the show
    premiere_year = show.get('premiered', '?')[:4] #Gets the premiere date of the show
    end_year = show.get('ended', '?')[:4] if show.get('status') == 'Ended' else '?' #Gets the end date of the show
    genres = ', '.join(show.get('genres', ['Unknown'])) #Gets the genres of the shows

    formatted_details = f"{show_name} ({premiere_year} - {end_year}, {genres})" #Formats the details of the show as specified
    return formatted_details #Returns the formatted details

def get_cast_by_id(show_id: int) -> list[dict]:
    """
    Get the cast for a show
    """
    castid = f"cast/{show_id}_cast.json" #Grabs the show json file from the cast folder
    return load_json(castid) #Returns the loaded json file from the cast folder

def format_cast(cast: list[dict]) -> str:
    """
    Format the cast
    """
    castid_formatted = "" #Empty string of the formatted cast info
    for actor in cast: #Loops through the json file of the cast folder
        castid_formatted += f'{actor["person"]["name"]} as {actor["character"]["name"]}\n' #Adds the cast name and character name to the empty string
    return castid_formatted #Returns the string with the added cast name and character name

def format_actor_info(actor_dict: dict) -> str:
    """
    Format the actor's information
    """
    if actor_dict is not None: #Checks to see if the character name and cast name is empty
        actor_info = (
            f"{actor_dict['person']['name']} " 
            f"({actor_dict['person']['gender']}, born {actor_dict['person']['birthday']} in {actor_dict['person']['country']['name']})"
            f" plays {actor_dict['character']['name']}"
        ) #Grabs the full data of the cast member
        return actor_info #Returns the full data of the cast member
    else:
        return "Actor not found" #If the dictionary was empty, return None

def main():
    shows_filename = 'tvshows.json' #Specifies the filename to be loaded
    shows = load_json(shows_filename) #Loads the file

    user_input = input("Enter the name of the show: ") #Grabs the userinput for the desired show
    selected_show_data = get_show_data_by_name(user_input, shows) #Checks to see if the userinput is in the loaded tvshow file
    
    if selected_show_data: #If the userinput is valid
        print(format_show_details(selected_show_data)) #Print the show details
        show_id = selected_show_data['id'] #Grabs the id of the show for the json file of the cast folder
        cast = get_cast_by_id(show_id) #Gets the cast list from the json file in the cast folder
        formatted_cast = format_cast(cast) #Formats the cast list into real name and character name
        print(f"Cast:\n{formatted_cast}") #Prints the formatted cast list
        actor_query = input("Enter the name of the actor or character: ") #From the printed list the user is asked to choose a character
        found_actor = find_actor(actor_query, cast) #Checks to see if the actor is in the list
        
        if found_actor: #If the actor is in the list
            actor_info = format_actor_info(found_actor) #Grabs the data of that actor from the json file in the cast folder
            print(actor_info) #Prints the data of the actor
        else:
            print("Can't find this actor or character in the cast!") #If a show was found, but not the actor print this error
    else:
        print("Show not found!") #If the show wasn't found print this error

if __name__ == '__main__':
    main()