class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1

    def __init__(self, title, author, rating, read=False, id=NO_ID):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.rating = rating
        self.read = read
        self.id=id


    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'
            #date_read = input('What date was this book read?') #assigns date the book was read

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Title: {} Author: {} Read: {} Rating: {}'
        return template.format(id_str, self.title, self.author, read_str, self.rating)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id and self.rating == other.rating
