# This should be an inner join onto customerlogin, but just select first, and last, with email
import sqlite3

from Account import Account
from datetime import datetime
from Transaction_Module import transaction
from AccountSummary import SummaryOfAccs


def viewAccountDetails(id):
    connection = sqlite3.connect('C:/Users/Joey/OneDrive/Documents/GitHub/Banking-App/venv/Banks.db', isolation_level=None)
    cursor = connection.cursor()
    query = "SELECT account_details.accountbalance, customerlogin.id, customerlogin.email, customerlogin.first, customerlogin.last " \
            "FROM account_details " \
            "INNER JOIN customerlogin ON account_details.customer_id = customerlogin.id " \
            "WHERE customerlogin.id = ?"
    cursor.execute(query, (id,))
    val = cursor.fetchone()

    acc = Account()
    acc.setAccountBalance(val[0])
    acc.setCustomerID(val[1])
    acc.setEmail(val[2])
    acc.setFirstName(val[3])
    acc.setLastName(val[4])
    return acc


def deposit(id, amount):
    # Select the amount first, then increment the amount
    connection = sqlite3.connect('C:/Users/Joey/OneDrive/Documents/GitHub/Banking-App/venv/Banks.db', isolation_level='DEFERRED')
    cursor = connection.cursor()
    query1 = "SELECT accountbalance FROM account_details WHERE customer_id = ?"
    cursor.execute(query1, (id,))
    val = cursor.fetchone()
    currBal = val[0]
    currBal = currBal + amount
    query = "UPDATE account_details SET accountbalance = ? WHERE customer_id = ?"
    cursor.execute(query, (currBal, id))
    connection.commit()
    print("Deposit Successful, Your new Balance is", currBal)

    currDate = datetime.now().strftime('%Y-%m-%d')

    # Insert transaction record into the database
    query2 = "INSERT INTO transactionhistory(date, type, chargedamount, id_number) VALUES (?, ?, ?, ?)"
    cursor.execute(query2, (currDate, 'Received', amount, id))
    connection.commit()


def withdraw(id, amount):
    connection = sqlite3.connect('C:/Users/Joey/OneDrive/Documents/GitHub/Banking-App/venv/Banks.db', isolation_level='DEFERRED')
    cursor = connection.cursor()
    query1 = "SELECT accountbalance FROM account_details WHERE customer_id = ?"
    cursor.execute(query1, (id,))
    val = cursor.fetchone()
    currBal = val[0]
    currBal = currBal - amount
    if currBal <= 0:
        return None
    else:
        query = "UPDATE account_details SET accountbalance = ? WHERE customer_id = ?"
        cursor.execute(query, (currBal, id))
        connection.commit()
        print("Withdraw Successful, Your new Balance is", currBal)

        currDate = datetime.now().strftime('%Y-%m-%d')

        # Insert transaction record into the database
        query2 = "INSERT INTO transactionhistory(date, type, chargedamount, id_number) VALUES (?, ?, ?, ?)"
        cursor.execute(query2, (currDate, 'Withdraw', amount, id))
        connection.commit()


def sendMoney(email, amount, id):
    connection = sqlite3.connect('C:/Users/Joey/OneDrive/Documents/GitHub/Banking-App/venv/Banks.db', isolation_level='DEFERRED')
    cursor = connection.cursor()

    # Check if the recipient exists in the database
    query = "SELECT account_details.accountbalance, customerlogin.id, customerlogin.email " \
            "FROM account_details " \
            "INNER JOIN customerlogin ON account_details.customer_id = customerlogin.id " \
            "WHERE customerlogin.email = ?"
    cursor.execute(query, (email,))
    val = cursor.fetchone()

    if val is None:
        print("USER NOT FOUND IN SYSTEM")
        return None

    recipientId = val[1]
    recipientMoney = val[0]

    query2 = "SELECT accountbalance FROM account_details WHERE customer_id = ?"
    cursor.execute(query2, (id,))
    ownVal = cursor.fetchone()
    userVal = ownVal[0]

    userVal = userVal - amount
    if userVal < 0:
        print("Insufficient Funds")
        return None
    recipientMoney = recipientMoney + amount

    query3 = "UPDATE account_details SET accountbalance = ? WHERE customer_id = ?"
    cursor.execute(query3, (recipientMoney, recipientId))
    cursor.execute(query3, (userVal, id))

    connection.commit()

    print("Transfer success, your new present balance is", userVal)
    currDate = datetime.now().strftime('%Y-%m-%d')

    # Need to make insertion statements for the one sending, and the one receiving the money in transactionhistory
    # Recipient First
    query4 = "INSERT INTO transactionhistory(date, type, chargedamount, id_number) VALUES (?,?,?,?)"
    cursor.execute(query4, (currDate, 'Received', amount, recipientId))
    connection.commit()

    query5 = "INSERT INTO transactionhistory(date, type, chargedamount, id_number) VALUES (?,?,?,?)"
    cursor.execute(query5, (currDate, 'Sent', amount, id))
    connection.commit()


# Plug the logic first into the other functionalities to insert into the transaction table upon withdraw, deposit, and transfer.
# Then make edits to view trans by id
def viewTransactionHistory(id):
    connection = sqlite3.connect('C:/Users/Joey/OneDrive/Documents/GitHub/Banking-App/venv/Banks.db', isolation_level='DEFERRED')
    cursor = connection.cursor()
    # This is going to return a list of rows, need to make a list of transaction objects
    query = "SELECT * FROM transactionhistory WHERE id_number = ?"
    cursor.execute(query, (id,))
    allTransactions = []
    TL = cursor.fetchall()
    for obj in TL:
        TransactionObject = transaction(obj[0], obj[1], obj[2], obj[3])
        allTransactions.append(TransactionObject)
    return allTransactions


def createAccount(first, last, email, password):
    connection = sqlite3.connect('C:/Users/Joey/OneDrive/Documents/GitHub/Banking-App/venv/Banks.db', isolation_level='DEFERRED')
    cursor = connection.cursor()
    query = "INSERT INTO customerlogin(email, password, first, last) VALUES(?,?,?,?)"
    cursor.execute(query, (email, password, first, last))
    connection.commit()
    query2 = "SELECT id FROM customerlogin WHERE email = ? and password = ?"
    cursor.execute(query2, (email, password))
    currId = cursor.fetchone()
    connection.commit()
    query3 = "INSERT INTO account_details(accountbalance, customer_id) VALUES(?,?)"
    cursor.execute(query3, (0, currId[0]))
    connection.commit()


def viewAllAccounts():
    connection = sqlite3.connect('C:/Users/Joey/OneDrive/Documents/GitHub/Banking-App/venv/Banks.db', isolation_level=None)
    cursor = connection.cursor()
    query = "SELECT customerlogin.first, customerlogin.last, customerlogin.email, account_details.accountbalance, account_details.customer_id " \
            "FROM customerlogin " \
            "INNER JOIN account_details ON customerlogin.id = account_details.customer_id"
    cursor.execute(query)
    accountSummaries = []
    for row in cursor.fetchall():
        summary = SummaryOfAccs(row[0], row[1], row[2], row[3], row[4])
        accountSummaries.append(summary)
    return accountSummaries
