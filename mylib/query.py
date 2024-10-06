"""Query the database"""

import sqlite3


def create():
    """CREATE"""
    conn = sqlite3.connect("nflReceivers.db")
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO nflReceivers (
        pfr_player_id,
        player_name,
        career_try,
        career_ranypa,
        career_wowy,
        bcs_rating) 
    VALUES ('SeweSt00','Steve Sewell',2247.446578,0.095783529,-0.729682089,NULL)"""
    )
    cursor.execute("SELECT * from nflReceivers WHERE player_name = 'Steve Sewell'")
    print("Inserted data into nflREceivers")
    print(cursor.fetchall())
    conn.close()
    return "Successful insertion into table"


def query():
    """Query the database for the top 5 rows table"""
    conn = sqlite3.connect("nflReceivers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nflReceivers ORDER BY career_try DESC LIMIT 5")
    print("Top 5 nflReceivers orderd by career tries:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


def update():
    """UPDATE TABLE"""
    conn = sqlite3.connect("nflReceivers.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE nflReceivers SET player_name = 'Jenny' WHERE id = 1")
    cursor.execute("SELECT * from nflReceivers WHERE id = 1")
    print("Updated name of player")
    print(cursor.fetchall())
    conn.close()
    return "Successfully updated"


def delete():
    """DELETE FROM TABLE"""
    conn = sqlite3.connect("nflReceivers.db")
    cursor = conn.cursor()
    cursor.execute("DELETE from nflReceivers WHERE id = 1")
    cursor.execute("SELECT * from nflReceivers WHERE id = 1")
    print("Deleted player")
    print(cursor.fetchall())
    conn.close()
    return "Successfully deleted"
