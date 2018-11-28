from __future__ import print_function
import json
import urllib.request

from typing import List, TextIO

from flask import Flask, request, render_template, json
from isbntools.app import *

import os
from book_rental_class import BookRental
import func_post_book

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search', methods=['POST'])
def my_form_post():
    form_text = request.form['form_text']
    search = form_text
    query = search.replace(' ', '+')
    isbn = isbn_from_words(query)

    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    with urllib.request.urlopen(base_api_link + isbn) as file:
        text = file.read()
    decoded_text = text.decode('utf-8')
    assert isinstance(decoded_text, object)
    json.loads(decoded_text)

    if isinstance(search, str):
        output = str(registry.bibformatters['labels'](meta(isbn)))
        f: TextIO = open("output.txt", "w")  # create output file in write mod
        f.write(output)  # write output to output file

        f = open("output.txt", 'r')
        lines: List[str] = f.readlines()
        for line in lines:  # strip labels from data line by line, remove empty space, prime for push to database
            if "Title" in line:
                global title
                title = line.replace("Title:", "").lstrip()
            if "Author" in line:
                global author
                author = line.replace("Author:", "").lstrip()
            if "ISBN" in line:
                global isbn_data
                isbn_data = line.replace("ISBN:", "").lstrip()
            if "Year" in line:
                global year
                year = line.replace("Year:", "").lstrip()
            if "Publisher" in line:
                global publisher
                publisher = line.replace("Publisher:", "".lstrip())

#                os.remove("output.txt")
                # HAVE OS REMOVE OUTPUT FILE AFTER GLOBALS ARE SET

    return render_template("search.html") % (title, author, isbn_data, year, publisher)

@app.route('/price', methods=['POST'])
def display_price_form():
    return render_template("price.html")


# RENDER PRICE CC: COMMENT ON SEARCH.HTML


@app.route('/date', methods=['POST'])
def record_price():
    price_text = request.form['price_text']
    global rental_value
    rental_value = price_text

    return render_template("dates.html")


@app.route('/dates', methods=['POST'])
def record_dates():
    count = str(len(open('main.json').readlines()) + 1)
    start_date = request.form['start_date']
    global start_date_value
    start_date_value = start_date
    end_date = request.form['end_date']
    global end_date_value
    end_date_value = end_date
    global owner_id
    owner_id = "000001"
    rental_id_value = count
    is_rented = "false"
    is_active = "true"
    book_rental_info = BookRental

    isbn = str(isbn_data)

    info2 = book_rental_info(isbn, title, author, rental_id_value, owner_id, rental_value, start_date, end_date)

    func_post_book.post_book(info2, is_active, is_rented, rental_id_value)

    return render_template("index.html")


@app.route('/rentals', methods=['POST'])
def rentals():

    with open("main.json", "r") as f:
        content = f.read()

    return render_template("rentals.html", content=content)


if __name__ == '__main__':
    app.run(debug=True)  # keep for debugging
