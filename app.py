from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add_book', methods=['POST'])
def add_book():
    # get book data from the request
    book_name = request.json["book_name"]
    author = request.json["author"]
    pub_year = request.json["pub_year"]
    genre = request.json["genre"]
    rating = request.form["rating"]

    # connect to db

    conn = sqlite3.connect("./library.db")
    c = conn.cursor()

    # insert book data into the database  
    c.execute("INSERT INTO books (book_name, author, pub_year, genre, rating) VALUES (?, ?, ?, ?, ?)",
              (book_name, author, pub_year, genre, rating))
    
    # commit changes and close connection
    conn.commit()
    conn.close()

    # return a json response for success
    return jsonify({'success': True})  

@app.route('/get_books', methods=['GET'])
def get_books():
    # connect to the db
    conn = sqlite3.connect("./library.db")
    c = conn.cursor()

    # get book data and close connection
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()

    # return books as JSON response
    return jsonify({"books": books}), 200

if __name__ == '__main__':
    app.run()
    
