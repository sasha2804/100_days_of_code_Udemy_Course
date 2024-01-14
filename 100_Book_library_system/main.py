
from data import Library



library = Library()



def main():  

    while True:
        print('1 add book')
        print('2 delete book')
        print('S save changes')
        print('3 display all books')
        print('4 search for a book')
        print('5 exit')
        choice = input('Enter command 1-5: ')

        if choice == "1":
            title = input('Enter title: ')
            author = input('Enter author: ')
            year = input('Enter year: ')            
            library.insert_book(title, author, year)

        if choice == "4":
            title = input('Enter title: ')
            author = input('Enter author: ')
            library.search_book(title, author)

            
        elif choice == "5":
            print('Exiting a program. Good Bye!')
            break



if __name__ == "__main__":
    main()