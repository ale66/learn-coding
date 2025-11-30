
# The Publisher Database example for learn-coding students

# Learn SQL SELECT queries and pandas integration

# %%

import mysql.connector
from mysql.connector import Error
import pandas as pd


# %%

## Database Connection Details

# check on the live coding session for the credentials

# the configuration dictionary
DB_CONFIG = {
    'host': 'db4free.net',
    'port': 3306,
    'database': 'learn_coding',  # from instructor
    'user': 'instructor',     # from instructor
    'password': 'Le@rn_cod1ng'  # from instructor
}

# %%

## Connect to the Database

### this functions is boilerplate: include and reuse

def connect_to_database():
    """Establish connection to the remote MySQL database"""

    try:
        print("Connecting to the publisher database...")
        connection = mysql.connector.connect(
            host = DB_CONFIG['host'],
            port = DB_CONFIG['port'],
            database = DB_CONFIG['database'],
            user = DB_CONFIG['user'],
            password = DB_CONFIG['password'],
            connection_timeout = 30
        )

        print("Connected successfully!")
        return connection
    
    except Error as e:
        print(f"Connection failed: {e}")

        return None

# %%

# Establish connection
conn = connect_to_database()

# %%

if conn and conn.is_connected():

    cursor = conn.cursor()
    
    # Query 1: View all authors
    
    cursor.execute("SELECT * FROM authors")

    results = cursor.fetchall()
    
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]:<20}, Born: {row[2]}, Sex: {row[3]}, Nationality: {row[4]}")
    
# %%

if conn and conn.is_connected():

    # Query 2: View books
    
    cursor.execute("SELECT title, genre, price FROM catalog LIMIT 10")

    results = cursor.fetchall()
    
    for row in results:
        print(f"{row[0]:<45} | {row[1]:<10} | ${row[2]:.2f}")

# %%

if conn and conn.is_connected():

    cursor = conn.cursor()
    
    # Query 3: Filter by genre
    cursor.execute("SELECT title, price FROM catalog WHERE genre = 'Mystery'")


    results = cursor.fetchall()
    
    for row in results:
        print(f"{row[0]:<45} | ${row[1]:.2f}")

# %%

if conn and conn.is_connected():

    cursor = conn.cursor()

    # Query 4: Filter by gender: female novelists
    
    cursor.execute("SELECT name, nationality FROM authors WHERE sex = 'F'")
    results = cursor.fetchall()
    
    for row in results:
        print(f"{row[0]:<20} | {row[1]}")
    
