from flask import Blueprint, request, jsonify
from app import db
from models import Book

bp = Blueprint('books', __name__)

@bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data.get('title'),
        author=data.get('author'),
        genre=data.get('genre'),
        published_date=data.get('published_date'),
        isbn=data.get('isbn'),
        total_copies=data.get('total_copies'),
        available_copies=data.get('available_copies')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'published_date': book.published_date,
            'isbn': book.isbn,
            'total_copies': book.total_copies,
            'available_copies': book.available_copies
        }
        for book in books
    ]
    return jsonify(result)

@bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.title = data.get('title')
    book.author = data.get('author')
    book.genre = data.get('genre')
    book.published_date = data.get('published_date')
    book.isbn = data.get('isbn')
    book.total_copies = data.get('total_copies')
    book.available_copies = data.get('available_copies')
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

@bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})
