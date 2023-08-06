class Login:
    id = None
    first = None
    last = None
    email = None
    password = None

    def __init__(self, id, first, last, email, password):
        self.id = id
        self.first = first
        self.last = last
        self.email = email
        self.password = password

        # Getters

    @property
    def first_name(self):
        return self.first

    @property
    def last_name(self):
        return self.last

    @property
    def email_address(self):
        return self.email

    @property
    def user_password(self):
        return self.password

    # Setters
    @first_name.setter
    def first_name(self, value):
        self.first = value

    @last_name.setter
    def last_name(self, value):
        self.last = value

    @email_address.setter
    def email_address(self, value):
        self.email = value

    @user_password.setter
    def user_password(self, value):
        self.password = value

    def getFirstName(self):
        return self.first

    def getLastName(self):
        return self.last

    def getId(self):
        return self.id

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def __str__(self):
        return f"First Name: {self.first}, Last Name: {self.last}, Email: {self.email}, Password: {self.password}"
