#get data for books rented out by a student
class StudentRentalRepository:

    #initialize the class attributes
    def __init__(self, owner_id, ISBN, checked_out, date_to_return):
        self.owner_id = owner_id
        self.ISBN = ISBN
        self.checked_out = checked_out
        self.date_to_return = date_to_return

    #find and return books checked out
    def FindRentedBooks(owner_id):
        rented_books =	{
          "owner_id": owner_id,
          "ISBN": 9783319712994,
          "checked_out": "Y",
          "date_to_return": 12202018
          }

        print(rented_books)
