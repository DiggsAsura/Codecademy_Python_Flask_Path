# 5. Introduction to SQL and Databses for Back-End Web Apps
# 3. Databases in Flask
# 3. Databases in Flask - Reading, Updating and Deleting
# 10. Review

''' 
Congratulations! This was maybe a challenging, but hopefully rewarding experience
for you.

In this lesson you learned how to:

1. query all entries with query.all(), or fetch an entry based on the value of its
   primary key with query.get(id)

2. retrieve related objects by using the attributes instantiated with db.relationship()
   in your model (Reader.query.get(123).reviews.all() ).

3. use filter and filter_by to select database entries based on some criterion
   (for example, Book.query.filter(Book.year = 2020).all() )

4. filter database entries by analyzing the patterns in their column values
   (for example, emails = Reader.query.filter(Reader.email.like('%.%@%').all())

5. add new entries to a database, or how to rollback in case the transaction had
   erroneous entries
   try:
    db.session.commit()
   except:
    db.session.rollback()

6. update existing entries in the database (for example Reader.query.get(3).email =
   "new_email@example.com")

7. remove database entries (for example, 
   db.session.delete(Reader.query.get(753))

8. combine database with your web application's templates (views).

The database that we sequentially built throughout the Flask-SQLAlchemy lesson has 
the following final schema:

<see 5_3_3_10-books-schema.jpg>

'''

# routes.py

from app import app
from app import db, Reader, Book, Review, Annotation
from flask import render_template, request, url_for, redirect

@app.route('/')
@app.route('/home')
def home():
  books = Book.query.all()
  return render_template('home.html', books=books)

@app.route('/profile/<int:user_id>')
def profile(user_id):
  reader = Reader.query.filter_by(id=user_id).first_or_404(description="There is no user with this ID.")
  return render_template('profile.html', reader=reader)

@app.route('/books/<year>')
def books(year):
  books = Books.query.filter_by(year=year)
  return render_template('display_books.html', year=year, books=books)

@app.route('/reviews/<int:review_id>')
def reviews(review_id):
  review = Review.query.filter_by(id=review_id).first_or_404(description="fuck off")
  return render_template('_review.html', review=review)
