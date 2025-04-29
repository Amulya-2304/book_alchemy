from flask_sqlalchemy import SQLAlchemy

# Initialize db object
db = SQLAlchemy()


# Define the Author model
class Author(db.Model):
    # Columns for the Author table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    date_of_death = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<Author {self.name}>"

    def __str__(self):
        return f"Author: {self.name}, Born: {self.birth_date}, Died: {self.date_of_death if self.date_of_death else 'N/A'}"


# Define the Book model
class Book(db.Model):
    # Columns for the Book table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    # Relationship with the Author model
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def __repr__(self):
        return f"<Book {self.title}>"

    def __str__(self):
        return f"Book: {self.title}, ISBN: {self.isbn}, Year: {self.publication_year}, Author: {self.author.name}"

