# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")

# `cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()`

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

with app.app_context():
    # CRUD: Create, Read, Update, Delete
    # 1. Create New Record
    # new_book = Book(title='Harry Potter and the chambers of secret', author='J. K. Rowling', rating='10')
    # db.session.add(new_book)
    # db.session.commit()

    # 2. Read all Records
    # result = db.session.execute(db.select(Book).order_by(Book.title))
    # all_books = result.scalars()
    # for book in all_books:
    #     print(f"Book title:{book.title}, author: {book.author}, and rating:{book.rating}")

    # 2b. Read a Particular record by Query
    # book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

    # 3. Update a Particular Record by Query
    # book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()

    # 3b. Update a Record by PRIMARY KEY
    book_id = 1
# with app.app_context():
    # book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    print(book_to_update.rating)
    db.session.commit()

    # 4. Delete a particular record by RPIMARY KEY
    book_id = 1
    # with app.app_context():
    #     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    #     # or book_to_delete = db.get_or_404(Book, book_id)
    #     db.session.delete(book_to_delete)
    #     db.session.commit()
