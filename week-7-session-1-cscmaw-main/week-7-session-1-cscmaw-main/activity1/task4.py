# Define a class Book with the following fields:
# (1) title - the book title
# (2) author - the author(s) of the book
# (3) ISBN - the International Standard Book Number, which is 10-13 digits long
# (4) availability - whether the book is available (True or False)
# When an instance of a Book is created, only the value to the first three fields are required
# for the __init__ method as the book is available when created.
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = True
    
    def dispaly_details(self):
        print(f'Title:{self.title}')
        print(f'Author:{self.author}')
        print(f'ISBN:{self.ISBN}')
        print(f'Availability:{self.availability}')

book1 = Book('Brave New World', 'sb.1', '114514')

book2 = Book('1984', 'sb.2', '1945')


# Once completed, create two instances of Book with the details of two of your favourite books.
# Write code to print the details of each books
