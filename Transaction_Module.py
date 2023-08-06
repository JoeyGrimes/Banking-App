class transaction:
    def __init__(self, date, transactionType, amount, idNumber):
        self._date = date
        self._transactionType = transactionType
        self._amount = amount
        self._idNumber = idNumber

    def getDate(self):
        return self._date

    def getTransactionType(self):
        return self._transactionType

    def getAmount(self):
        return self._amount

    def getIdNumber(self):
        return self._idNumber

    def setDate(self, date):
        self._date = date

    def setTransactionType(self, transactionType):
        self._transactionType = transactionType

    def setAmount(self, amount):
        self._amount = amount

    def setIdNumber(self, idNumber):
        self._idNumber = idNumber
