import pymysql as sql

def lend_book(user_id,book_id,copy_number):
    connection = sql.connect(
        host="localhost",
        user='root',
        password='Govind@1950',
        db='library'
    )
    cursor = connection.cursor()
    # The book has a column called lent which has a boolean value, so we are setting it to True for the
    # specific combination of book_id and copy_number
    cursor.execute(f"UPDATE books SET lent = True WHERE book_id = {book_id} AND copy_number = {copy_number}")
    # We are also adding the user to the user table where his user_id, name, department_name, book_id,
    # copy_number are stored
    # We are getting the username from the student table where the user_id is stored
    cursor.execute(f"SELECT username FROM student WHERE user_id = {user_id}")
    username = cursor.fetchone()[0]
    # We are adding the user to thje user table
    # the department name is represented by the 3rd and 4th character of the user_id in the student table
    # so we are extracting that from the user_id
    department_name = user_id[2:4]
    cursor.execute(f"INSERT INTO users VALUES({user_id},'{username}',{department_name},{book_id},{copy_number})")
    connection.commit()
    connection.close()
