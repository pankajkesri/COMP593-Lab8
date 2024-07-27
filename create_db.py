
"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS  people (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER,
                   email TEXT NOT NULL UNIQUE,
                   created_at TEXT NOT NULL,
                   updated_at TEXT NOT NULL
                   )
    ''')
    connection.commit()
    connection.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    faker = Faker()
    current_time = datetime.now().strftime('%Y-%m-%y %H:%M:%S')
    
    people = []
    for _ in range(200):
        name = faker.name()
        age = faker.random_int(min=1, max=100)
        email = faker.email()
        created_at = current_time
        updated_at = current_time
        people.append((name, age, email, created_at, updated_at))

    # Insert fake people into the people table
    cursor.executemany('''
        INSERT INTO people (name, age, email, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
    ''', people)

    connection.commit()
    connection.close()

if __name__ == '__main__':
   main()