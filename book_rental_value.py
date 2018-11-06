import json
from rental_class import BookRental

# a Python object (dict):

isbn = input("ISBN ")
rental_id = input("Rental ID ")
owner_id = input("Owner ID ")
rental_value = input("Enter book rental value: ")

rental_info = BookRental(isbn, rental_id, owner_id, rental_value)

rental_info.fnc_rental_value()

# a Python object:

x = {
    "isbn": str(rental_info.isbn),
    "rental id": str(rental_info.rental_id),
    "owner id": str(rental_info.owner_id),
    "rental value": str(rental_info.rental_value)
}

# convert into JSON:

y = json.dumps(x)

# result is a JSON string

print(y)


