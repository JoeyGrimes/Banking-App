from LoginStruct import Login
import LoginDaoImpl


class LoginService:

    def customerLogin(self, email, password):
        return LoginDaoImpl.customerLogin(email, password)

    def employeeLogin(self, email, password):
        return LoginDaoImpl.employeeLogin(email, password)


