import psycopg2

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

# Insert dummy data into the author table
insert_author_query = '''
    INSERT INTO booksort.author (name)
    VALUES 
        ('Author 1'),
        ('Author 2'),
        ('Author 3')
    ON CONFLICT (name) DO NOTHING
'''
cursor.execute(insert_author_query)

# Insert dummy data into the book table
insert_book_query = '''
    INSERT INTO booksort.book (title, genre, author_id)
    VALUES 
        ('Book 1', 'Fiction', 1),
        ('Book 2', 'Non-Fiction', 2),
        ('Book 3', 'Mystery', 3)
'''
cursor.execute(insert_book_query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
