import json
from Crypto.PublicKey import RSA
from Crypto import Random

# creating the json object that will serve the information to the webpage


def post_book(book_rental_info, is_rented, is_active, rental_id_value):
    x = {
        "isbn": str(book_rental_info.isbn),
        "book author": str(book_rental_info.author),
        "book title": str(book_rental_info.book_title),
        "rental id": str(book_rental_info.rental_id),
        "owner id": str(book_rental_info.owner_id),
        "rental value": str(book_rental_info.rental_value),
        "start date": str(book_rental_info.start_date),
        "end date": str(book_rental_info.end_date),
        "is rented": str(is_rented),
        "is active": str(is_active),
    }
    # convert into JSON:

    y = book_rental_info.owner_id + "_" + rental_id_value + " " + json.dumps(x)
    f = open('main.json', 'a')
    f.write(y + '\n')

def encrypt_file():
    #generate public/ private keys
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    public_key = key.publickey()

    #encrypt input string from user
    encrypt_file = public_key.encrypt("main.json", 32)

    #save text file containing book information to an encrypted text file

    enc_file = open("main.json", "w")
    enc_file.write(str(encrypt_file))
    enc_file.close()
    return enc_file

def decrypt_file(enc_file):
    decrypt=''
    
    dec_file = key.decrypt(encrypt_file)
    decrypted_file = open("main.json", "w")
    decrypted_file.write(str(dec_file))
    decrypted_file.close()
    decrypted_file = open("output.txt", "r")
    return decrypted_file

