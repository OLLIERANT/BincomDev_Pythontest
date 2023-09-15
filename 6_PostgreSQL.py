#!/usr/bin/python3
"""
Script that saves the colours and their frequencies
in postgresql database
"""

import psycopg2
from config import config

# create DATABASE if it doesn't exist
CREATE DATABASE Bincom_Dev;

# Connect to the PostgreSQL database using the psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="Bincom_Dev",
    user="postgres",
    password="passwd")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

def create_tables():
    """ create tables in the PostgreSQL database"""
    CREATE TABLE color_frequencies (
    color VARCHAR(255) PRIMARY KEY,
    frequency INT
);

# insert data into the table color_frequencies pair of the database
INSERT INTO color_frequencies (color, frequency) VALUES
("ARSH", 1)
("GREEN", 10)
("YELLOW", 5)
("BROWN", 6)
("BLUE", 31)
("PINK", 5)
("RED", 9)
("WHITE", 16)
("ORANGE", 9 )
("CREAM", 2)
("BLACK", 1)

for color, frequency in color_data:
    cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

if __name__ == '__main__':
    create_tables()
