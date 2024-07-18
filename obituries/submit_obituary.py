

import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='obituary_platform'
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def insert_obituary(connection, obituary_data):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO obituaries (name, dob, dod, content, author) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, obituary_data)
        connection.commit()
        cursor.close()
        return True
    except Error as e:
        print(f"Error inserting data into the database: {e}")
        return False

def main():
    id = ""
    name = "John Doe"
    date_of_birth = "1990-01-01"
    date_of_death = "2024-07-15"
    content = "Lorem ipsum dolor sit amet..."
    author = "Jane Smith"
    submission_date = ""
    slug = ""

    obituary_data = (name, date_of_birth, date_of_death, content, author,  submission_date, slug)

    db_connection = connect_to_database()
    if db_connection:
        if insert_obituary(db_connection, obituary_data):
            print("Obituary submitted successfully!")
        else:
            print("Error submitting obituary. Please try again later.")
        db_connection.close()

if __name__ == "__main__":
    main()
