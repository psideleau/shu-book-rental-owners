#allows a user to request status of rented out books

#import function to find books rented out
from student_rental_repository import StudentRentalRepository

#create an instance of the StudentRentalRepository class
rented_books = StudentRentalRepository

#hard code owner_id
owner_id = 2345789

#call function to list books rented out
rented_books.FindRentedBooks(owner_id)
