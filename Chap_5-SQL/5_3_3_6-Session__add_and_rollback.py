# 5. Introduction to SQL and Databses for Back-End Web Apps
# 3. Databases in Flask
# 3. Databases in Flask - Reading, Updating and Deleting
# 6. Session: add and rollback

''' 
A set of operations such as addition, removal, or updating database entries
is called a database transaction. A database session consists of one or more 
transactions. The act of committing ends a transaction by saving the transaction
permanently to the database. In contrast, rollback rejects the pending transaction
and changes are not permanently saved in the database.

In Flask-SQLAlchemy, a database is changed in the context of a session, which 
can be accessed as the session attribute of the database instance. An entry is
added to a session with the add() method. The changes in a session are 
permanently written to a database when .commit() is executed.

For example, we create new readers and would like to add them to our database:


from app import db, Reader
new_reader1 = Reader(name = "Nova", surname = "Yeni", email = "nova.yeni@example.com")
new_reader2 = Reader(name = "Nova", surname = "Yuni", email = "nova.yeni@example.com")
new_reader3 = Reader( name = "Tom", surname = "Grey", email = "tom.grey@example.edu")


Note that we didn't specify the primary key id value. Primary keys don't have to be
specified explicitly, and the values are automatically generated after the
transaction is commited.

Adding each new entry to the database has the same pattern:


db.session.add(new_reader1)
try:
  db.session.commit()
except:
  db.session.rollback()


Notice that we surrounded db.session.commit() with a try-except block. Why did
we do that? If you look more carefully, new_reader1 and new_reader2 have the
same e-mail, and when we declared the Reader model, we made the e-mail column
unique (see the app.py file). As a consequence, we want to undo the most recent
addition to the transaction by using db.session.rollback() and continue with 
other additions without interruption.
'''

from app import db, Reader #notice we import db here as well
import add_data #we use this script to recreate the database, put all the entries so every time you run this script you get the same result

#creating new readers
new_reader1 = Reader(name='Nova', surname='Yeni', email='nova.yeni@sample.com')
new_reader2 = Reader(name='Nova', surname='Yuni', email='nova.yeni@sample.com')
new_reader3 = Reader(name='Tom', surname='Grey', email='tom.grey@example.edu')

print('Before addition')
[print(reader.id, reader.email) for reader in Reader.query.all()]

print('\nNote that before commiting, the id of the new reader is: ', new_reader1.id,'\n')

#adding the first reader - the commit should succeed
db.session.add(new_reader1)
try:
  db.session.commit()
  print(f'Commit succeded. {new_reader1} added to the database permanently. The exception was not raised.\n')
except:
  db.session.rollback()

#adding the second reader - the commit should FAIL because e-mail should be unique
db.session.add(new_reader2)
try:
  db.session.commit()
except Exception as ex:
  print(f"The commit of {new_reader2} didn't succeed. Duplicate primary key values. We will empty the current session.\n")
  print(f"The error is the following: {ex}")
  db.session.rollback()

#adding the third reader - the commit should succeed
db.session.add(new_reader3)
try:
  db.session.commit()
  print(f"Commit succeeded. {new_reader3} added to the database permanently. Theexception was not raised.\n")
except Exception as ex:
  db.session.rollback()

print(f"\nNote that after commiting, the id of the new readers is now {new_reader1.id} \n")

#print all the readers after the addition, and we see nova.yeni@sample.com there, but not twice
[print(reader.id, reader.email) for reader in Reader.query.all()]
print(f"\nThe new readers Nova Yeni and Tom Grey are in the database. Notice that Nova Yeni doesn't appear twice.\n")

print("\nCheckpoint 1: create a new_reader")
new_reader = Reader(name='Peter', surname='Johnsen', email='peter.johnson@example.com')

print("\nCheckpoint 2: add the new reader to the database:")
db.session.add(new_reader)

print("\nCheckpoint 3: commit and rollback if exception is raise:")
try:
  db.session.commit()
except:
  db.session.rollback()