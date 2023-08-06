import sqlite3

from LoginStruct import Login


def customerLogin(email, password):
    connection = sqlite3.connect('C:/Users/Joey/PycharmProjects/BankApplication/venv/Banks.db', isolation_level=None)
    cursor = connection.cursor()
    query = "SELECT * FROM customerlogin where email =  ? AND password = ?"
    cursor.execute(query, (email, password))
    val = cursor.fetchone()
    if val is None:
        return None
    else:
        acc = Login(val[0], val[3], val[4], val[1], val[2])
        return acc

# Check if the row exists in database, and if it does throw all the fields into an empty login Object, eitherwise
# Just return null immediately


def employeeLogin(email, password):
    connection = sqlite3.connect('C:/Users/Joey/PycharmProjects/BankApplication/venv/Banks.db', isolation_level=None)
    cursor = connection.cursor()
    query = "SELECT * FROM employeelogin where email =  ? AND password = ?"
    cursor.execute(query, (email, password))
    val = cursor.fetchone()
    if val is None:
        return None
    else:
        acc = Login(val[0], val[1], val[2], val[3], val[4])
        return acc
