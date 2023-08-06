DROP TABLE IF EXISTS employeelogin;
DROP TABLE IF EXISTS customerlogin;
DROP TABLE IF EXISTS account_details;
DROP TABLE IF EXISTS transactionhistory;



CREATE TABLE employeelogin(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);

CREATE TABLE customerlogin(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);

CREATE TABLE account_details (
    accountbalance INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customerlogin(id) ON DELETE CASCADE
);

CREATE TABLE transactionhistory (
    date TEXT NOT NULL,
    type TEXT NOT NULL,
    chargedamount INT NOT NULL,
    id_number INT NOT NULL,
    FOREIGN KEY (id_number) REFERENCES customerlogin(id) ON DELETE CASCADE

);

PRAGMA foreign_keys = ON;

INSERT INTO employeelogin (email, password, first, last)
VALUES
    ('admin@matadorbanking.com', 'admin1', 'Admin', 'Admin'),
    ('emp', 'emp', 'emp', 'emp');

INSERT INTO customerlogin (email, password, first, last)
VALUES
('test', 'test', 'test', 'test'),
('danrobertson@gmail.com', 'password', 'Dan', 'Smith' );




INSERT INTO account_details(accountbalance, customer_id)
VALUES
(10000, 1),
(50000, 2)





