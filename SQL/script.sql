CREATE TABLE IF NOT EXISTS books (
    id VARCHAR(25) NOT NULL PRIMARY KEY UNIQUE,
    bname VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    lent BOOLEAN DEFAULT FALSE,
    genre VARCHAR(255) NOT NULL
);








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

SELECT * FROM student;


