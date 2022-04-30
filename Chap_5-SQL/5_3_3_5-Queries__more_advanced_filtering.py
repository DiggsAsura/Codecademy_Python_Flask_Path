# 5. Introduction to SQL and Databses for Back-End Web Apps
# 3. Databases in Flask
# 3. Databases in Flask - Reading, Updating and Deleting
# 5. Queries: more advanced filtering

''' 
Flask-SQLAlchemy allows more compled queries and operations such as checking 
wheter a column starts, or ends, with some string. One can also order retrieved
queries by some criterion. There are many more possible queries, but here we cover
only some of them.

For example, to retrieve e-mails that end with edu we do:


education = Reader.query.filter(Reader.email.endswith('edu')).all()


To retrieve all the readers with e-mails that contain a '.' before the '@' symbol
we use .like():


emails = Reader.query.filter(Reader.email.like('%.%'@%')).all()


You might recognize the like operator from SQL. It is used to search for a 
specified pattern in a column. The wildcard % represents zero, one, or 
multiple characters.

In the two examples above, we used methods on the column of the table
(SQLAlchemy's ColumnElement).

To order books by year we use the .order_by() method on Query:


ordered_books = Book.query.order_by(Book.year).all()


We suggest checking the SQLAlchemy Core + ORM documentation to see other
querying options.
'''

from app import db, Book, Reader, Review

# retrieve all reader with .edu e-mails
education = Reader.query.filter(Reader.email.endswith('edu')).all()
print(education)

# retrieve all readers with e-mails that contain a . before the @ symbol
emails = Reader.query.filter(Reader.email.like('%.%@%')).all()
print('\nReaders with e-mail having a . before the @ symbol:')
[print(e) for e in emails]

# order all books by year
ordered_books = Book.query.order_by(Book.year).all()
print('\nBook ordered by year:')
[print(book.title, book.year) for book in ordered_books]

print('\nCheckpoint 1: your code here below:')
s_names = Reader.query.filter(Reader.surname.endswith('s')).all()
print(s_names)

print('\nCheckpoint 2: your code here below:')
sample_emails = Reader.query.filter(Reader.email.like('%@sample%')).all()
print(sample_emails)

print('\nCheckpoint 3: your code here below:')
ordered_reviews = Review.query.order_by(Review.stars).all()

