class BookRental:
    # Creating Book Rental class

    def __init__(self, isbn, book_title, author, rental_id, owner_id, rental_value, start_date, end_date,):
        self.isbn = isbn
        self.book_title = book_title
        self.author = author
        self.rental_id = rental_id
        self.owner_id = owner_id  # Owner will be passed in value from the login group. Hard coding for now
        self.rental_value = rental_value
        self.start_date = start_date
        self.end_date = end_date

    # Function to pass in values from the ISBN search and set variables needed for posting book rental

    def get_rental_info(self):
        self.isbn = input("ISBN: ")  # pass ISBN from search and set in this variable
        self.author = input("author: ")  # pass Author from search and set in this variable
        self.book_title = input("Title: ")  # pass title from search and set in this variable
        self.owner_id = "owner id: "  # no variable to be passed yet. This would come from login group
        self.rental_id = input("Enter rental ID: ")  # Owner assigns rental value to book
        self.rental_value = input("Enter a rental value: ")  # Owner sets the start and end period for book rental
        self.start_date = input(" Enter your rental period start date: ")
        self.end_date = input(" Enter your rental period end date: ")

    # Creating an instance of the class 'BookRental' and setting the variables. This will essentially create a
        # Python dict.
        rental_info = BookRental(self.isbn, self.author, self.book_title, self.rental_id, self.owner_id,
                                 self.rental_value, self.start_date, self.end_date)
    # Returning value to be used for posting the book to the group of student renters
        return rental_info
