import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, redirect, request



database = "Data/MediaDatabase.db"
games = []
movies = []
tvshows = []



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn



def read_from_db():
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
        except Error as e:
            print(e)
    
    c.execute("""SELECT * FROM games ORDER BY sort_time DESC""")
    global games
    games = [x for x in c.fetchall()]

    c.execute("""SELECT * FROM movies ORDER BY sort_time DESC""")
    global movies
    movies = [x for x in c.fetchall()]

    c.execute("""SELECT * FROM tvshows ORDER BY sort_time DESC""")
    global tvshows
    tvshows = [x for x in c.fetchall()]
        

def toggle_game(id):
    id = id[2::]
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
        except Error as e:
            print(e)

    c.execute("""SELECT played FROM games WHERE name = ? """, (id,))
    current = c.fetchone()[0]
    if current == "No":
        newstatus = "Yes"
    else:
        newstatus = "No"
    
    c.execute("""UPDATE games SET played = ? WHERE name = ? """, (newstatus, id,))
    conn.commit()


def toggle_movie(id):
    id = id[2::]
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
        except Error as e:
            print(e)

    c.execute("""SELECT watched FROM movies WHERE name = ? """, (id,))
    current = c.fetchone()[0]
    if current == "No":
        newstatus = "Yes"
    else:
        newstatus = "No"
    
    c.execute("""UPDATE movies SET watched = ? WHERE name = ? """, (newstatus, id,))
    conn.commit()


def toggle_tvshow(id):
    id = id[2::]
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
        except Error as e:
            print(e)

    c.execute("""SELECT watched FROM tvshows WHERE name = ? """, (id,))
    current = c.fetchone()[0]
    if current == "No":
        newstatus = "Yes"
    else:
        newstatus = "No"
    
    c.execute("""UPDATE tvshows SET watched = ? WHERE name = ? """, (newstatus, id,))
    conn.commit()








app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    read_from_db()
    return render_template("index.html", games = games, movies = movies, tvshows = tvshows)


@app.route("/update", methods=["POST"])
def update():
    id = request.form.get("id")
    if id[0] == "G":
        toggle_game(id)
    elif id[0] == "M":
        toggle_movie(id)
    elif id[0] == "T":
        toggle_tvshow(id)

    return redirect("/")



if __name__ == "__main__":
    app.run(port=5100)
    #app.run(host="0.0.0.0", port=5100, debug=False)
