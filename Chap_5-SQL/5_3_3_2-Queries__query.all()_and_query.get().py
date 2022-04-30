# 5. Introduction to SQL and Databses for Back-End Web Apps
# 3. Databases in Flask
# 3. Databases in Flask - Reading, Updating and Deleting
# 2. Queries: query.all() and query.get()

'''
Querying a database table with Flask SQLAlchemy is done through the query property
of the Model class. To get all entries from a model called TableName we run 
TableName.query.all(). Often you know the primary key (unique identifier) value
of entries you want to fetch. To get an entry with some primary key value ID from
model TableName you run TableName.query.get(ID).

For example, to get all the entries from the Reader table we do the following:


readers = Reader.query.all()


Similary, to get a reader with id = 123 we do the following:


reader = Reader.query.get(123)


We assign the result of the .get() method to a variable because through that variable
we can access the entry's attributes. For example:


reader = Reader.query.get(450)
print(reader.name)


Now you see the amazing convenience of using ORM: database tables are simply 
treated as Python classes and databases entries are Python objects. For example,
you can easily use a for loop to loop through all the readers and print 
their name:


readers = Reader.query.all()
for reader in readers:
  print(reader.name)

'''

from app import db, Book, Reader, Review, Annotation

readers = Reader.query.all()
print(readers)

reader = Reader.query.get(123)
print(reader)

print('\nPrint all the readers in a loop:')
for reader in readers:
  print(reader.email)

#or inline
# [print(reader.email) for reader in readers]


print('\nCheckpoint1: fetching all the reviews')
reviews = Review.query.all()

print('\nCheckpoint2: looping through all the reviews and printing their text')
for review in reviews:
  print(review.text)

print('\nCheckpoint3: fetching a book with id = 13 using the get() function')
book_1 = Book.query.get(13)