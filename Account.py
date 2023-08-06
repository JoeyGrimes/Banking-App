class Account:
    def __init__(self):
        self._accountBalance = None
        self._customer_id = None
        self._email = None
        self._firstName = None
        self._lastName = None

    # Getters and setters for accountBalance
    def getAccountBalance(self):
        return self._accountBalance

    def setAccountBalance(self, balance):
        self._accountBalance = balance

    # Getters and setters for customer_id
    def getCustomerID(self):
        return self._customer_id

    def setCustomerID(self, customer_id):
        self._customer_id = customer_id

    # Getters and setters for email
    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    # Getters and setters for firstName
    def getFirstName(self):
        return self._firstName

    def setFirstName(self, first_name):
        self._firstName = first_name

    # Getters and setters for lastName
    def getLastName(self):
        return self._lastName

    def setLastName(self, last_name):
        self._lastName = last_name
