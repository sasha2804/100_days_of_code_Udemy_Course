import sqlite3

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


class Library:
    def __init__(self, db_name='100_Book_library_system/Data_Base/library_system.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_books_table()

    def create_books_table(self):
        create_books_table_query = """
            CREATE TABLE IF NOT EXISTS books_list_table (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT, 
                year INTEGER
            );
            """
        self.cursor.execute(create_books_table_query)
        self.connection.commit()
    
    def insert_book(self, title, author, year):
        # book = Book()
        insert_data_query = """
        INSERT INTO books_list_table (title, author, year) VALUES (?, ?, ?);
        """
        data_to_insert = (title, author, year)
        self.cursor.execute(insert_data_query, data_to_insert)
        # Commit the changes to the database
        self.connection.commit()


        # Example: Query data from the table
        select_data_query = """
        SELECT * FROM books_list_table;
        """
        self.cursor.execute(select_data_query)

        # Fetch all rows from the result set
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)


        # Close the cursor and connection
        self.cursor.close()
        self.connection.close()

    
    def search_book(self, title, author):
        


        pass
    
    




    
    


