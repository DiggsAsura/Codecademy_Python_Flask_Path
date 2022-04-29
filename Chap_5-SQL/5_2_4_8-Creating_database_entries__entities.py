# 5. Introduction to SQL and Databses for Back-End Web Apps
# 2. Queries
# 4. Databases in Flask
# 8. Creating database entries: entities

''' 
Now that we initialized our database schema, the next step is to start creating
entries that will later populate the database. The beauty of SQLAlchemy Object
Relational Mapper (ORM) is that our database entries are simply created as 
instances of Python classes representing the declared models.

We will create our objects in a separate file called create_object.py. To create
objects representing model entries, we first need to import the models from 
the app.py file:


from app import Reader, Book, Review


We can create an object of class Book in the following way:


b1 = Book(id=123, title='Demian', author_name='Hermann', author_surname='Hesse', month="February", year=2020)


An example object of class Reader could be:


r1 = Reader(id=343, name='Ann', surname='Adams', email='ann.adams@example.com')


Thanks to the ORM, creating database entries is the same as creating Python objects.

We interact with database entries in the way we interact with Python objects. In case
we want to access a specific attribute or column, we do it in the same way we would
access attributes of Python objects: by using . (dot) notation:


print("My first reader:", r1.name) # prints My first reader: Ann

'''

# This is a separate Python script in which we practice creating objects
# You can also perform these operations in command-line terminal

from app import Reader, Book, Review

b1 = Book(id=123, title='Demian', author_name='Hermann', author_surname='Hesse', month='February', year=2020)
r1 = Reader(id=342, name='Ann', surname='Adams', email='ann.adams@example.com')

print(f'My first reader: {r1.name}')

b2 = Book(id=533, title='The Stranger', author_name='Albert', author_surname='Camus', month='April', year=2019)
r2 = Reader(id=756, name='Sam', surname='Adams', email='sam.adams@example.com')

print(b2.author_name)
print(len(r2.email))
