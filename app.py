from flask import Flask, render_template, request, redirect, url_for, flash
from data_models import db, Author, Book

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Route to delete a book
@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    # Find the book by its ID
    book = Book.query.get_or_404(book_id)

    # Get the author associated with the book
    author = book.author

    # Delete the book
    db.session.delete(book)
    db.session.commit()

    # Check if the author has any other books
    if not Author.query.filter_by(id=author.id).first():
        # If the author has no other books, delete the author
        db.session.delete(author)
        db.session.commit()

    flash(f'Book "{book.title}" deleted successfully!', 'success')
    return redirect(url_for('home'))

# Home route to display books
@app.route('/', methods=['GET', 'POST'])
def home():
    sort_by = request.args.get('sort_by', 'title')  # Default sorting by title
    search_query = request.args.get('search', '')  # Get the search query from the form

    if sort_by == 'author':
        books = Book.query.filter(Book.title.like(f'%{search_query}%')).order_by(Book.author_id).all()
    else:
        books = Book.query.filter(Book.title.like(f'%{search_query}%')).order_by(Book.title).all()

    return render_template('home.html', books=books, sort_by=sort_by, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)
