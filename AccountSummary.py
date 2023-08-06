class SummaryOfAccs:
    def __init__(self, firstName, lastName, email, accountBalance, customerId):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._accountBalance = accountBalance
        self._customerId = customerId

    def getFirstName(self):
        return self._firstName

    def setFirstName(self, value):
        self._firstName = value

    def getLastName(self):
        return self._lastName

    def setLastName(self, value):
        self._lastName = value

    def getEmail(self):
        return self._email

    def setEmail(self, value):
        self._email = value

    def getAccountBalance(self):
        return self._accountBalance

    def setAccountBalance(self, value):
        self._accountBalance = value

    def getCustomerId(self):
        return self._customerId

    def setCustomerId(self, value):
        self._customerId = value
