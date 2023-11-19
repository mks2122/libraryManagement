import datetime
import pymysql as sql

def lend_books(book_id,user_id):
    """
    :param book_id:
    :param user_id:
    :return: None
    This function takes in a user_ID and a particular Book_ID and lends the books to the user
    """
    connection = sql.connect(
        host="localhost",
        user='root',
        password='Kausik@2204',
        db='library'
    )
    try:
        cursor = connection.cursor()
        # (Name,ID)
        cursor.execute(f"SELECT bname FROM books WHERE id={book_id}")
        book_name = cursor.fetchone()[0]

        # Writing into the user table
        cursor.execute(f"SELECT name FROM student WHERE roll='{user_id}'")
        user_name = cursor.fetchone()[0]

        # Updating the lent column of books table
        cursor.execute(f"UPDATE books SET lent={True} WHERE id={book_id}")

        # Updating the user table
        cursor.execute(f"INSERT INTO library.user (uid, uname, dname, bookid) VALUES('{user_id}', '{user_name}', '{user_id[2:4]}', '{book_id}')")

        # Updating the drem table
        # Get the current date
        today = datetime.datetime.today()
        # Calculate the due date for the book
        due_date = today + datetime.timedelta(days=21)
        cursor.execute(f"INSERT INTO library.drem (bkid, userid, rented, due, ext) VALUES('{book_id}', '{user_id}', '{today}', '{due_date}',0)")
        print("Succesfully Updated")
    finally:
        connection.commit()
        connection.close()


def return_book(book_id,user_id):
    """
    This function helps the user return a book back to the library.
    :param book_id:
    :param user_id:
    :return: None
    """
    connection = sql.connect(
        host="localhost",
        user='root',
        password='Govind@1950',
        db='library'
    )

    # Updating the drem table
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM library.drem WHERE bkid='{book_id}' AND userid='{user_id}'")

        #Deleting from the user table
        cursor.execute(f"DELETE FROM library.user WHERE uid='{user_id}' AND bookid='{book_id}'")

        # Updating the books table
        cursor.execute(f"UPDATE library.books WHERE id='{book_id}' SET lent={False}")

        print("Succesfully Updated")
    finally:
        connection.commit()
        connection.close()



# return_book("0060887966",'22AM112')

def fetch_all_books():
    """
    This function retuns a list of all books available in the library.
    This is useful for the admin view the books in the library.
    :return: list of all books
    """
    global books
    connection = sql.connect(
        host='localhost',
        user='root',
        password='Kausik@2204',
        db='library'
    )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM books WHERE lent=0")
        books = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        return books
def fetch_availablity_of_book(identifier, by_name=True):
    """
    This function returns the availability of a book in the library.
    :param identifier: Book name or book ID based on the search type.
    :param by_name: If True, search by book name; if False, search by book ID.
    :return: Book information if found, None otherwise.
    """
    connection = sql.connect(
        host='localhost',
        user='root',
        password='Kausik@2204',
        db='library'
    )
    cursor = connection.cursor()

    try:
        if by_name:
            cursor.execute(f"SELECT * FROM books WHERE bname='{identifier}'")
        else:
            cursor.execute(f"SELECT * FROM books WHERE id='{identifier}'")

        book = cursor.fetchone()
        return book

    except Exception as e:
        print(e)
    finally:
        connection.close()
def fetch_lent_books():
    """
    This function returns a list of all the lent books with additional details such as
    the user information, date lent, date of return, and number of reminders.
    :return: list of lent books with details
    """
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Kausik@2204',
        db='library'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)  # Using DictCursor for a dictionary-like result

    try:
        # Using INNER JOIN to combine information from the 'books', 'user', and 'drem' tables
        query = """
        SELECT books.id AS book_id, books.bname AS book_name, books.genre,
                   user.uid AS user_id, user.uname AS user_name,
                   drem.rented AS date_lent, drem.due AS date_of_return, drem.ext AS reminders_sent
            FROM books
            INNER JOIN user ON books.id = user.bookid
            INNER JOIN drem ON books.id = drem.bkid
            WHERE books.lent = 1"""
        cursor.execute(query)
        lent_books_details = cursor.fetchall()

        return lent_books_details

    except Exception as e:
        print(e)
    finally:
        connection.close()

print(fetch_availablity_of_book("The Prophet",by_name=True))
lend_books("0060887966",'22AM112')