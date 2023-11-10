CREATE TABLE IF NOT EXISTS books (
    id VARCHAR(25) NOT NULL PRIMARY KEY UNIQUE,
    bname VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    lent BOOLEAN DEFAULT FALSE,
    genre VARCHAR(255) NOT NULL
);

SELECT * FROM books;


CREATE TABLE user (
    uid VARCHAR(15) NOT NULL,
    uname VARCHAR(255) NOT NULL,
    dname VARCHAR(6) NOT NULL,
    bookid VARCHAR(25) NOT NULL,
    PRIMARY KEY (uid, bookid)
);



CREATE TABLE drem (
    bkid VARCHAR(25) NOT NULL,
    userid VARCHAR(15) NOT NULL,
    rented DATE NOT NULL,
    due DATE NOT NULL,
    ext INT NOT NULL,
    FOREIGN KEY (bkid) REFERENCES books(id),
    FOREIGN KEY (userid) REFERENCES user(uid)
);





CREATE TABLE IF NOT EXISTS student (
    roll VARCHAR(8) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL
);

SELECT * FROM student WHERE roll="22AM112";

INSERT INTO user (uid, uname, dname, bookid)
VALUES (
    "22AM112",
        (SELECT name FROM student WHERE roll="22AM112"),
        "AML",
        (SELECT id FROM books WHERE bname="The Alchemist" ORDER BY id DESC LIMIT 1)
       );

SELECT * FROM user INNER JOIN books ON user.bookid=books.id WHERE user.uid="22AM112";
# deleting the duplicate entries
# CREATE TABLE temp_books (
#     bname VARCHAR(255) NOT NULL,
#     PRIMARY KEY (bname)
# );
#
# INSERT INTO temp_books (bname)
# SELECT bname
# FROM books
# GROUP BY bname
# HAVING COUNT(*) > 1;
#
#
# DELETE FROM books
# WHERE bname IN (
#     SELECT bname
#     FROM temp_books
# );
#
# DROP TABLE temp_books;
#
SELECT * FROM books;
