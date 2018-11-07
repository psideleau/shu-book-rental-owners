# Import BookRental class from Book_Rental_Class.py file
from book_rental_class import BookRental
# Import the function that posts the book for the student group to call
import func_post_book

# creating an instance of the book class and calling the funtion to set the variables and assign the book information
# to the book class instance (called book_rental_info)

# creating instance of Book Class
book_rental_info = BookRental
# calling function to get book information and assigning it to the instance of the book class- book_rental_info
book_rental_info.get_rental_info(book_rental_info)

# function to take the book information and post it for the student group
func_post_book.post_book(book_rental_info)
