from flask import Flask, render_template, request, jsonify, redirect, url_for
from db import books_collection
from bson.json_util import dumps
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    categories = books_collection.distinct("language_code")
    return render_template('index.html', categories=categories)

@app.route('/books', methods=['GET'])
def get_books():
    lang = request.args.get('language')
    query = {"language_code": lang} if lang else {}
    books = list(books_collection.find(query))
    return dumps(books)

@app.route('/book/<book_id>', methods=['GET'])
def get_book(book_id):
    book = books_collection.find_one({"_id": book_id})
    return dumps(book)

@app.route('/admin/add', methods=['POST'])
def add_book():
    data = request.json
    books_collection.insert_one(data)
    return jsonify({"message": "Book added successfully"})

@app.route('/admin/delete/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = books_collection.delete_one({"_id": book_id})
    return jsonify({"deleted": result.deleted_count})

@app.route('/admin/update/<book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    books_collection.update_one({"_id": book_id}, {"$set": data})
    return jsonify({"message": "Book updated successfully"})

@app.route('/admin')
def admin_panel():
    books = list(books_collection.find())
    return render_template('admin.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)
