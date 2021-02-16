import os, time
import json
from datetime import datetime



# Writes the selected list (Movies, Games, or TV Shows) to a .json file
def write_json(filename, list):
    with open(f"Data/{filename}.json", "w") as filehandle:
        json.dump(list, filehandle)


# The functions below do not overwrite existing entries, only add to the lists if the entires aren't already present
# This is important as they won't overwrite the "played" or "watched" flags that may be set

# Update the games json file with the current directory listing
def update_games_json(gamespath):

    # Checks if a games json file already exists
    # If so, loads the json file as the variable game_list
    # If not, initializes the variable game_list as a blank list
    if os.path.isfile("data/gamelist.json"):
        with open("data/gamelist.json", "r") as filehandle:
            game_list = json.load(filehandle)
    else:
        game_list = []

    # Creates 2 variables, existing_titles (titles that are already in the json file)
    # and game_name_list (titles of games currently in the games directory)
    existing_titles = [x["name"] for x in game_list]
    game_name_list = [x for x in os.listdir(gamespath)]

    # Checks if games in game_name_list are already in existing_titles
    # If not, adds them to the game_list including the name, download date, and played status
    for x in game_name_list:
        if x not in existing_titles:
            creation_time = (datetime.fromtimestamp(os.path.getctime(os.path.join(gamespath, x)))).strftime("%m/%d/%y %H:%M:%S")
            sort_time = (datetime.fromtimestamp(os.path.getctime(os.path.join(gamespath, x)))).strftime("%y/%m/%d/%H/%M/%S")
            obj = {"name" : x, "downloaded_on" : creation_time, "sort_time" : sort_time, "played" : "No"}
            game_list.append(obj)

    # Checks if games in game_list are no longer in the directory (ie if something was moved or deleted)
    # If so, iterates through game_list to find name match and removes record
    for x in existing_titles:
        if x not in game_name_list:
            i = 0
            for y in game_list:
                if x == y["name"]:
                    game_list.pop(i)
                    break
                else:
                    i += 1

    # Calls the write_json function to write game_list to the json file
    write_json("gamelist", game_list)


# Updates the moves json file with the current directory listing
def update_movies_json(moviespath):

    # Checks if a movies json file already exists
    # If so, loads the json file as the variable movie_list
    # Otherwise initializes the variable movie_list as a blank list
    if os.path.isfile("data/movielist.json"):
        with open("data/movielist.json", "r") as filehandle:
            movie_list = json.load(filehandle)
    else:
        movie_list = []

    # Creates 2 variables, existing_titles (titles that are already in the json file)
    # and game_name_list (titles of movies currently in the movies directory)
    existing_titles = [x["name"] for x in movie_list]
    movie_name_list = [x for x in os.listdir(moviespath)]
    
    # Checks if movies in movie_name_list are already in existing_titles
    # If not, adds them to the movie_list including the name, download date, and played status
    for x in movie_name_list:
        if x not in existing_titles:
            creation_time = (datetime.fromtimestamp(os.path.getctime(os.path.join(moviespath, x)))).strftime("%m/%d/%y %H:%M:%S")
            sort_time = (datetime.fromtimestamp(os.path.getctime(os.path.join(moviespath, x)))).strftime("%y/%m/%d/%H/%M/%S")
            obj = {"name" : x, "downloaded_on" : creation_time, "sort_time" : sort_time, "watched" : "No"}
            movie_list.append(obj)


    # Checks if movies in movie_list are no longer in the directory (ie if something was moved or deleted)
    # If so, iterates through movie_list to find name match and removes record
    for x in existing_titles:
        if x not in movie_name_list:
            i = 0
            for y in movie_list:
                if x == y["name"]:
                    movie_list.pop(i)
                    break
                else:
                    i += 1
    
    # Calls the write_json function to write movie_list to the json file
    write_json("movielist", movie_list)


# Updates the tvshows json file with the current directory listing
def update_tvshows_json(tvshowspath):

    # Checks if a tvshow json file already exists
    # If so, loads the json file as the variable tvshow_list
    # Otherwise initializes the variable tvshow_list as a blank list
    if os.path.isfile("data/tvshowlist.json"):
        with open("data/tvshowlist.json", "r") as filehandle:
            tvshow_list = json.load(filehandle)
    else:
        tvshow_list = []

    # Creates 2 variables, existing_titles (titles that are already in the json file)
    # and tvshow_name_list (titles of tvshows currently in the tvshows directory)
    existing_titles = [x["name"] for x in tvshow_list]
    tvshow_name_list = []
    
    # Using os.walk to check for files in all subdirectories, creates a variable called filelist that contains all filenames
    for root, dirs, files in os.walk(tvshowspath):
        filelist = [x for x in os.listdir(f"{root}") if os.path.isfile(os.path.join(f"{root}", x))]
        # If filelist isn't blank, append all filenames from filelist to tvshow_name_list
        if filelist != []:
            for x in filelist:
                tvshow_name_list.append(x)
                # Checks if tvshows in tvshow_name_list are already in existing_titles
                # If not, adds them to the tvshow_list including the name, download date, and played status
                if x not in existing_titles:
                    creation_time = datetime.fromtimestamp(os.path.getctime(os.path.join(f"{root}", x))).strftime("%m/%d/%y %H:%M:%S")
                    sort_time = datetime.fromtimestamp(os.path.getctime(os.path.join(f"{root}", x))).strftime("%y/%m/%d/%H/%M/%S")
                    obj = {"name" : x, "downloaded_on" : creation_time, "sort_time" : sort_time, "watched" : "No"}
                    tvshow_list.append(obj)

    # Checks if tvshows in tvshow_list are no longer in the directory (ie if something was moved or deleted)
    # If so, iterates through tvshow_list to find name match and removes record
    for x in existing_titles:
        if x not in tvshow_name_list:
            i = 0
            for y in tvshow_list:
                if x == y["name"]:
                    tvshow_list.pop(i)
                    break
                else:
                    i += 1

    # Calls the write_json function to write tvshow_list to the json file
    write_json("tvshowlist", tvshow_list)

