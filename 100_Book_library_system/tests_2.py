import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('100_Book_library_system/Data_Base/library_system.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named 'students'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')

# Insert data into the 'students' table
cursor.execute('''
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
''', ('John Doe', 20, 'A'))

cursor.execute('''
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
''', ('Jane Smith', 22, 'B'))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()