from flask import Flask, g, request, jsonify
import psycopg2

app = Flask(__name__)

# Database configuration
DATABASE = {
    'dbname': "postgres",
    'user': "postgres",
    'password': "Kassou104",
    'host': "localhost",
    'port': "5432"
}

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**DATABASE)
        g.cursor = g.db.cursor()
    return g.db, g.cursor

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.cursor.close()
        g.db.close()

# Retrieve all books
@app.route('/books', methods=['GET'])
# Retrieve all books
@app.route('/books', methods=['GET'])
def get_all_books():
    try:
        # Query the database to retrieve all books
        db, cursor = get_db()
        query = '''
            SELECT title, genre, name as author
            FROM booksort.book
            JOIN booksort.author ON book.author_id = author.id;
        '''
        cursor.execute(query)
        books = cursor.fetchall()

        # Convert the result to a list of dictionaries
        book_list = [{'title': title, 'genre': book_genre, 'author': author} for title, book_genre, author in books]

        return jsonify(book_list)

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        return jsonify({'error': 'An error occurred while processing the request'}), 500
    finally:
        # Do not close the connection here, it will be handled by the teardown_appcontext
        pass


# Retrieve books by genre
@app.route('/books/<string:genre>', methods=['GET'])
def get_books_by_genre(genre):
    try:
        # Query the database to retrieve books by genre
        db, cursor = get_db()
        query = '''
            SELECT title, genre, name as author
            FROM booksort.book
            JOIN booksort.author ON book.author_id = author.id
            WHERE genre = %s;
        '''
        cursor.execute(query, (genre,))
        books = cursor.fetchall()

        # Convert the result to a list of dictionaries
        book_list = [{'title': title, 'genre': book_genre, 'author': author} for title, book_genre, author in books]

        return jsonify(book_list)

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        return jsonify({'error': 'An error occurred while processing the request'}), 500
    finally:
        # Do not close the connection here, it will be handled by the teardown_appcontext
        pass

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
