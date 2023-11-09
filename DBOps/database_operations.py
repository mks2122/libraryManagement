import pymysql as sql

def lend_book(user_id,book_id,copy_number):
    connection = sql.connect(
        host="localhost",
        user='root',
        password='Govind@1950',
        db='library'
    )
    cursor = connection.cursor()
    try:
        # The book has a column called lent which has a boolean value, so we are setting it to True for the
        # specific combination of book_id and copy_number
        cursor.execute(f"UPDATE books SET lent = True WHERE id = {book_id} AND cno = {copy_number}")
        # We are also adding the user to the user table where his user_id, name, department_name, book_id,
        # copy_number are stored
        # We are getting the username from the student table where the user_id is stored
        cursor.execute(f"SELECT name FROM student WHERE roll = {user_id}")
        username = cursor.fetchone()[0]
        # We are adding the user to thjs user table
        # the department name is represented by the 3rd and 4th character of the user_id in the student table
        # so we are extracting that from the user_id
        department_name = user_id[2:4]
        cursor.execute(f"INSERT INTO user VALUES({user_id},'{username}',{department_name},{book_id},{copy_number})")
        # We are updating thedrem table which stores the due reminer
        # We are setting the due date to 15 days from the current date
        cursor.execute(f"INSERT INTO drem VALUES({book_id},{user_id},CURRENT_DATE(),DATE_ADD(CURDATE(), INTERVAL 15 DAY),0)")
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def return_book(user_id,book_id,copy_number):
    connection = connection = sql.connect(
        host="localhost",
        user='root',
        password='Govind@1950',
        db='library'
    )
    cursor = connection.cursor()
    try:
        # We are setting the lent column of the book to False
        cursor.execute(f"UPDATE books SET lent = False WHERE id = {book_id} AND cno = {copy_number}")
        # We are deleting the user from the user table
        cursor.execute(f"DELETE FROM user WHERE uid = {user_id} AND bookid = {book_id} AND bcno = {copy_number}")
        # We are deleting the user from the drem table
        cursor.execute(f"DELETE FROM drem WHERE userid = {user_id} AND bkid = {book_id}")

        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
