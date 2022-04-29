# 5. Introduction to SQL and Databses for Back-End Web Apps
# 2. Queries
# 4. Databases in Flask
# 7. Putting it all together: initializing the database

''' 
When you ran your application in the previous exercises you might have relized
that there is no database file created in the application folder. The reason
is simple: we need to explicitly initialize the database accorind to the 
models declared.

We can initialize our database in two ways:

1. Using the interactive Python shell.

- In the command-line terminal, navigate to the application folder and enter
  Python's interactive mode:
  
  $ python3
  
- Import the database instance db from app.py:

  >>>> from app import db

  (this assumes the application file is called app.py)

- Create all database tables according to the declared models:

  >>>> db.create_all()


2. From within the application file. After all the models have been specified the
   database is initialized by adding db.create_all() to the main program. The 
   command is written after all the defined models.

The result of db.create_all() is that the database schema is created representing
our declared models. After running the command, you should see your database file
in the path and with the name you set in the SQLALCHEMY_DATABASE_URI configuration
field. 
'''

# 1. python3
# 2. from app import db
# 3. db.create_all()

