

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

def retrieve_obituaries(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM obituaries;"
        cursor.execute(query)
        obituaries = cursor.fetchall()
        cursor.close()
        return obituaries
    except Error as e:
        print(f"Error retrieving obituaries: {e}")
        return []

def main():
    db_connection = connect_to_database()
    if db_connection:
        obituaries = retrieve_obituaries(db_connection)
        db_connection.close()

        
        print("<html>")
        print("<head>")
        print("<style>")
        print("table {")
        print("    width: 100%;")
        print("    border-collapse: collapse;")
        print("}")
        print("th, td {")
        print("    border: 1px solid #ddd;")
        print("    padding: 8px;")
        print("    text-align: left;")
        print("}")
        print("th {")
        print("    background-color: #f2f2f2;")
        print("}")
        print("</style>")
        print("</head>")
        print("<body>")
        print("<table>")
        print("<tr><th>Name</th><th>Date of Birth</th><th>Date of Death</th><th>Content</th><th>Author</th></tr>")
        for obituary in obituaries:
            print(f"<tr><td>{obituary[0]}</td><td>{obituary[1]}</td><td>{obituary[2]}</td><td>{obituary[3]}</td><td>{obituary[4]}</td></tr>")
        print("</table>")
        print("</body>")
        print("</html>")

if __name__ == "__main__":
    main()
