# 5. Introduction to SQL and Databses for Back-End Web Apps
# 3. Databases in Flask
# 3. Databases in Flask - Reading, Updating and Deleting
# 1. Interacting with a Database

''' 
Your database has a number of readers who subscribed to your book club and some
books you already assigned to be read. Also some of your readers wrote reviews
about the books and some of them might have some annotations made while reading
their books on an eReader. The schema representing the database is in the image
on the right.

<see img 5_3_3_1-books-schema.jpg>

Say you want to list all the books you suggested or list all the subscribed
readers. Or let each subscriber see only the reviews they wrote. When new
people subscribe to your web service, you need to add them to your database,
or when they unsubscribe delete them. If you made a mistake in changing your
database, you probably want to undo the changes or 'rollback' to the previous
correct state. When your subscribers change their e-mail, you need to update 
your database. Or you need to filter out the books your club read in the year 
2019 and only calculate average ratings of those. These are all the most common
interactions with a database, and in this lesson, you will learn how to perform
them in Flask-SQLAlchemy.

Throughout this exercise we will provide you with a database containing some 
entries for you to query, but you will learn how to add more entries, and remove
some, on the way.

Can't wait? let's go.

'''

# I understand the importance. I hope I can learn this shit!