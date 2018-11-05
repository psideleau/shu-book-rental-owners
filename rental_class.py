class BookRental:

    def __init__(self, isbn, rental_id, owner_id, rental_value):
        self.isbn = isbn
        self.rental_id = rental_id
        self.owner_id = owner_id
        self.rental_value = rental_value

    def fnc_rental_value(self):
        print("Isbn: " + self.isbn + " rental value: " + self.rental_value)
