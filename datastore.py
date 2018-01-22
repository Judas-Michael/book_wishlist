
import os
import json
from book import Book

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.json')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0

def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    try :
        with open(BOOKS_FILE_NAME) as f:
            data = json.loads(f.read())
            make_book_list(data)
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass


    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        f.write(json.dumps(output_data))

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    if len(kwargs) == 0:
        return book_list
		search_function = input("Enter a search function") #enters custom search function
    if search_function in kwargs: #instead of read can return any search keyword
        read_books = [ book for book in book_list if book.read == kwargs['read'] ]
        return read_books


def sort_booklist(param):

    global book_list

    if param == 1:
        book_list = sorted(book_list, key=lambda book: book.title)
    elif param == 2:
        book_list = sorted(book_list, key=lambda book: book.author)
    elif param == 3:
        book_list = sorted(book_list, key=lambda book: book.id)


def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id()
    book_list.append(book)
    if book.read == 'yes':
        print("This book has been read!") #posts this message if the added book has been read


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, book_rating):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            book.rating = book_rating
            return True

    return False # return False if book id is not found


def delete_book(book_id):
    ''' Retrieve from db by id, remove book, return result '''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book_list.remove(book)
            return True

    else:
        return False


def make_book_list(json_data):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    for obj in json_data:
        title = obj['title']
        author = obj['author']
        read = False
        id = obj['id']
        if obj['read'] == 'True':
            read = True
            rating = obj['rating']
            date_read = obj['date_read']
            book = Book(title, author, read, rating, date_read, int(id))
        else:
            book = Book(title, author, read, int(id))

        book_list.append(book)

def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    json_data = [{"title": book.title,
                  "author": book.author,
                  "read": str(book.read),
                  "rating": book.rating,
                  "date_read": book.date_read,
                  "id": str(book.id)} for book in book_list]

    return json_data
