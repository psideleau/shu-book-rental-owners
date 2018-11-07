import json
# creating the json object that will serve the information to the webpage


def post_book(book_rental_info):
    x = {
        "isbn": str(book_rental_info.isbn),
        "book author": str(book_rental_info.author),
        "book title": str(book_rental_info.book_title),
        "rental id": str(book_rental_info.rental_id),
        "owner id": str(book_rental_info.owner_id),
        "rental value": str(book_rental_info.rental_value),
        "start date": str(book_rental_info.start_date),
        "end date": str(book_rental_info.end_date)
    }
    # convert into JSON:

    book_post = json.dumps(x)
    # result is a JSON string

    print(book_post)
