# 5. Introduction to SQL and Databses for Back-End Web Apps
# 2. Queries
# 4. Databases in Flask
# 9. Creating database entries: relationships

'''
Creating objects for tables that have forign keys is not much different from the
usual creation of Python objects. 

Consider that we have the following objects already created:


b1 = Book(id = 123, title = 'Demian', author_name = 'Hermann', author_surname = 'Hesse')
b2 = Book(id = 533, title = 'The stranger', author_name = 'Albert', author_surname = 'Camus')
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')
r2 = Reader(id = 312, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.com')


To create an entry in the Review table, in addition to specify a review text
and a rating, we also need to specify which reader wrote the review, and for
which book. In other words, we need to specify values for the review's forign
keys reviewer_id and book_id that represents primary keys in Reader and Book,
respectively.


rev1 = Review(id=435, text='This book is amazing...', stars=5, reviewer_id=r1.id, book_id=b1.id)


In the example above we see that the review is written by Reader instance r1 for
Book instance b1. We again used Python's dot notation to access the id attribute of 
r1 and b1 objects.

Note: in the future, when creating database entries you don't need to specify the
primary key value explicitly, if you don't have a preference for the values. When
adding entries to a database, a primary key value will be automatically generated,
unless specified. In the next lesson, we will see how to add entries to our 
database.
'''

from app import Reader, Book, Review

b1 = Book(id=123, title='Demian', author_name='Hermann', author_surname='Hesse')
b2 = Book(id=533, title='The Stranger', author_name='Albert', author_surname='Camus')
r1 = Reader(id=342, name='Ann', surname='Adams', email='ann.adams@example.com')
r2 = Reader(id=312, name='Sam', surname='Adams', email='sam.adams@example.com')

rev1 = Review(id=435, text='This book is amazing...', stars=5, reviewer_id=r1.id, book_id=b1.id)
print(rev1)
print(rev1.text)
print(rev1.book_id)

rev2 = Review(id=450, text='This book is difficult!', stars=2, reviewer_id=r2.id, book_id=b2.id)
print(len(rev2.text.split()))
