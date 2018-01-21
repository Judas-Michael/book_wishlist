#Main program

import ui, datastore
from book import Book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        del_book()

    elif choice == '6':
        sort_books()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    rating = ''
    while rating not in range(1,5):
        try:
            rating = int(input("How many stars do you give this book? (1-5): "))
            if rating not in range(1,5):
                print('Number not within valid range.')
        except ValueError:
            print('Please enter a valid integer')

    rating = ('*' * rating)

    if datastore.set_read(book_id, rating):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))


def del_book():
    '''Get info from user, delete selected book if exists, display result'''
    book_id = ui.ask_for_book_id()
    if datastore.delete_book(book_id):
        ui.message('Book deleted')
    else:
        ui.message('Book id not found in database')


def sort_books():
    '''Get input from user, sort list by selection (author or title)'''
    print('''Sort by what?
        1. Title
        2. Author
        3. Book ID
    ''')

    sort_by = int(input('Enter your selection: '))
    if sort_by in range(1,4):
        datastore.sort_booklist(sort_by)
        ui.message('Book list sorted.')
    else:
        ui.message('Please enter a valid selection.')
        sort_books()


def quit():
    '''Perform shutdown tasks'''
    datastore.shutdown()
    ui.message('Bye!')


def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
