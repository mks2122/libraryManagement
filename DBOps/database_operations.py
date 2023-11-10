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
        password='Govind@1950',
        db='library'
    )
    try:
        cursor = connection.cursor()
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
    finally:
        connection.commit()
        connection.close()



lend_books("0060887966",'22AM112')


