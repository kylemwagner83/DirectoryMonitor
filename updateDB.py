# Imports
import sqlite3
from sqlite3 import Error
import json
import os


# Global Variables
database = "Data/MediaDatabase.db"
game_list = []
movie_list = []
tvshow_list = []



# Functions
def load_games_json():
    if os.path.isfile("data/gamelist.json"):
        with open("data/gamelist.json", "r") as filehandle:
            global game_list
            game_list = json.load(filehandle)

def load_movies_json():
    if os.path.isfile("data/movielist.json"):
        with open("data/movielist.json", "r") as filehandle:
            global movie_list
            movie_list = json.load(filehandle)

def load_tvshows_json():
    if os.path.isfile("data/tvshowlist.json"):
        with open("data/tvshowlist.json", "r") as filehandle:
            global tvshow_list
            tvshow_list = json.load(filehandle)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_my_tables():
    sql_create_games_table = """ CREATE TABLE IF NOT EXISTS games (
                                    name text PRIMARY KEY,
                                    downloaded_on text,
                                    sort_time,
                                    played text
                                ); """

    sql_create_movies_table = """ CREATE TABLE IF NOT EXISTS movies (
                                    name text PRIMARY KEY,
                                    downloaded_on text,
                                    sort_time,
                                    watched text
                                ); """

    sql_create_tvshows_table = """ CREATE TABLE IF NOT EXISTS tvshows (
                                    name text PRIMARY KEY,
                                    downloaded_on text,
                                    sort_time,
                                    watched text
                                ); """

    conn = create_connection(database)                                
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_games_table)
            c.execute(sql_create_movies_table)
            c.execute(sql_create_tvshows_table)
        except Error as e:
            print(e)
    else:
        print("Could not create connection to database")


def update_games_db():
    load_games_json()
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
        except Error as e:
            print(e)
    # Checks database and removes entires if they aren't also listed in the json file
    c.execute("""SELECT name FROM games""")
    db_names = [x[0] for x in c.fetchall()]
    json_names = [x["name"] for x in game_list]
    for name in db_names:
        if name not in json_names:
            c.execute("""DELETE FROM games WHERE name=?""", (name,))
            print(f"{name} removed from database")
    conn.commit()
    # Checks json file and adds entries to database if they aren't already there
    for x in game_list:
        name = x["name"]
        downloaded_on = x["downloaded_on"]
        sort_time = x["sort_time"]
        played = x["played"]
        c.execute("""SELECT name FROM games WHERE name=?""",(name,))
        result = c.fetchone()
        if result == None:
            c.execute("""INSERT INTO games(name,downloaded_on,sort_time,played) VALUES(?,?,?,?)""", (name, downloaded_on, sort_time, played,))
            print(f"{name} added to database")
    conn.commit()


def update_movies_db():
    load_movies_json()
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
        except Error as e:
            print(e)
    # Checks database and removes entires if they aren't also listed in the json file
    c.execute("""SELECT name FROM movies""")
    db_names = [x[0] for x in c.fetchall()]
    json_names = [x["name"] for x in movie_list]
    for name in db_names:
        if name not in json_names:
            c.execute("""DELETE FROM movies WHERE name=?""", (name,))
            print(f"{name} removed from database")
    conn.commit()
    # Checks json file and adds entries to database if they aren't already there
    for x in movie_list:
        name = x["name"]
        downloaded_on = x["downloaded_on"]
        sort_time = x["sort_time"]
        watched = x["watched"]
        c.execute("""SELECT name FROM movies WHERE name=?""",(name,))
        result = c.fetchone()
        if result == None:
            c.execute("""INSERT INTO movies(name,downloaded_on,sort_time,watched) VALUES(?,?,?,?)""", (name, downloaded_on, sort_time, watched,))
            print(f"{name} added to database")
    conn.commit()


def update_tvshows_db():
    load_tvshows_json()
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
        except Error as e:
            print(e)
    # Checks database and removes entires if they aren't also listed in the json file
    c.execute("""SELECT name FROM tvshows""")
    db_names = [x[0] for x in c.fetchall()]
    json_names = [x["name"] for x in tvshow_list]
    for name in db_names:
        if name not in json_names:
            c.execute("""DELETE FROM tvshows WHERE name=?""", (name,))
            print(f"{name} removed from database")
    conn.commit()
    # Checks json file and adds entries to database if they aren't already there
    for x in tvshow_list:
        name = x["name"]
        downloaded_on = x["downloaded_on"]
        sort_time = x["sort_time"]
        watched = x["watched"]
        c.execute("""SELECT name FROM tvshows WHERE name=?""",(name,))
        result = c.fetchone()
        if result == None:
            c.execute("""INSERT INTO tvshows(name,downloaded_on,sort_time,watched) VALUES(?,?,?,?)""", (name, downloaded_on, sort_time, watched,))
            print(f"{name} added to database")
    conn.commit()

create_my_tables()