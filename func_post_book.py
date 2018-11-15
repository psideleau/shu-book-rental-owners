import json
# creating the json object that will serve the information to the webpage

# function to post book


def post_book(book_rental_info):
    # By default owner status and rental status are set at time of book posting
    owner_status = "active"
    rental_status = "checked in"
    # Gets user input for book posting and converts to json string
    x = {
        "isbn": str(book_rental_info.isbn),
        "book author": str(book_rental_info.author),
        "book title": str(book_rental_info.book_title),
        "rental id": str(book_rental_info.rental_id),
        "owner id": str(book_rental_info.owner_id),
        "rental value": str(book_rental_info.rental_value),
        "start date": str(book_rental_info.start_date),
        "end date": str(book_rental_info.end_date),
        "owner status": str(owner_status),
        "rental status": str(rental_status)
    }
    # convert into JSON:

    book_post = json.dumps(x)
    # result is a JSON string
    # creates book file or appends book file if it exists with the posting information

    try:
        file = open('books.txt', 'r')
        file_exists = str('yes')
        file.close()
    except FileNotFoundError:
        file_exists = str('no')

    if file_exists == 'no':
        file = open("books.txt", "w+")
        file.close()

    file = open("books.txt", "a")
    file.write("\n" + book_post)
    file.close()
    file = open("books.txt", "r")
    book_contents = file.read()
    # print(book_contents)
    # print(book_post)
    return book_contents

# put book file into list format for searching and to updated with rented book

# function for getting the rental ID. This will be replaced with an API call
# to the student renters group


def input_rental_id():
    rental_id = input("Enter rental ID: ")
    return rental_id





