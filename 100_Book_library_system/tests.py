import sqlite3

connection = sqlite3.connect('100_Book_library_system/Data_Base/library_system.db')
cursor = connection.cursor()

# Example: Create a table


create_table_query = """
CREATE TABLE IF NOT EXISTS books_list_table (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT, 
    year INTEGER
);
"""




cursor.execute(create_table_query)

# Commit the changes to the database
connection.commit()


# Example: Insert data into the table
insert_data_query = """
INSERT INTO books_list_table (title, author, year) VALUES (?, ?, ?);
"""

data_to_insert = ("Goal", "Eliyahoo Goldrat", 2005)
cursor.execute(insert_data_query, data_to_insert)

# Commit the changes to the database
connection.commit()

# Example: Query data from the table
select_data_query = """
SELECT * FROM books_list_table;
"""
cursor.execute(select_data_query)

# Fetch all rows from the result set
rows = cursor.fetchall()

for row in rows:
    print(row)


# Close the cursor and connection
cursor.close()
connection.close()