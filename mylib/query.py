"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows table"""
    conn = sqlite3.connect("nflReceivers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nflReceivers")
    print("Top 5 rows of the nflReceivers table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
