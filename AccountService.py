import AccountDaoImpl


class AccountService:
    def viewAccountDetails(self, id):
        return AccountDaoImpl.viewAccountDetails(id)

    def deposit(self, id, amount):
        return AccountDaoImpl.deposit(id, amount)

    def withdraw(self, id, amount):
        return AccountDaoImpl.withdraw(id, amount)

    def sendMoney(self, email, amount, id):
        return AccountDaoImpl.sendMoney(email, amount, id)

    def viewTransactionHistory(self, id):
        return AccountDaoImpl.viewTransactionHistory(id)

    def createAccount(self, first, last, email, password):
        return AccountDaoImpl.createAccount(first, last, email, password,)

    def viewAllAccounts(self):
        return AccountDaoImpl.viewAllAccounts()
