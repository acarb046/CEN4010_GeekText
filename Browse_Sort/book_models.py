from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Kassou104",
    host="localhost",
    port="5432"
)

# Create a cursor
cursor = conn.cursor()


@app.route('/books', methods=['GET'])
def get_books_by_genre():
    # Get the 'genre' parameter from the request
    genre = request.args.get('genre')

    if not genre:
        return jsonify({'error': 'Genre parameter is missing'}), 400

    # Query the database to retrieve books by genre
    query = '''
        SELECT title, genre, name as author
        FROM booksort.book
        JOIN booksort.author ON book.author_id = author.author_id
        WHERE genre = %s;
    '''
    cursor.execute(query, (genre,))
    books = cursor.fetchall()

    # Convert the result to a list of dictionaries
    book_list = [{'title': title, 'genre': book_genre, 'author': author} for title, book_genre, author in books]

    return jsonify(book_list)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
