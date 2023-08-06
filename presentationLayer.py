# Joe Grimes
# CIS 131
# 7/30/2023

import sys
import AccountService
import LoginService


def main():
    loginService = LoginService.LoginService()
    accountService = AccountService.AccountService()
    bull = """   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣶⣦⣤⡀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠿⠿⠟⠿⠿⠿⠛⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣄⣀⣀⣀⣀⣤⣤⣤⣶⣖⣒⣻⣿⣭⣭⣭⣭⣭⣭⣍⣛⡓⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠒⠛⠛⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠲⣌⡳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠋⠉⠉⠉⠙⠒⠶⠤⢤⣤⣤⣀⣤⣤⣴⡾⢁⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣡⣤⣼⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⡀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠙⣷⡀⢀⣱⣀⣹⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣿⣷⣤⣄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠿⢿⡿⠿⠿⠿⣿⣷⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢹⡀⠀⣤⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣶⣼⣧⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠛⠛⠛⠋⣹⣿⣿⣷⡄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡉⠛⢻⣿⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⢠⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠿⢛⣿⣿⣿⣿⣿⣿⣿⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⢸⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢁⣠⣭⣍⡀⠀⠀⠀⠀⠀⠈⠙⠛⠻⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠈⣿⣿⠟⠿⠶⠀⠀⠀⠀⣠⣶⢀⣤⣤⣶⣶⣤⣄⡴⠋⠀⠀⢘⡟⣴⣶⣶⣦⣶⣶⣤⣤⣀⣀⢹⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⠀⣤⡀⠰⣿⣿⣿⣎⠙⠻⣿⣿⣿⣿⠀⠀⠀⣾⣿⣧⣉⣉⣽⣿⣿⣛⡿⢿⣿⣿⠀⠀⠉⠛⠶⠦⣤⣄⠤⢖⡆
⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⢰⣿⣿⣿⣷⣤⣴⣿⣿⣿⣿⣿⣿⣷⠀⠀⠈⠛⠋⢿⣄⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣶⣶⣦⣤⣄⣀⣠⡤⠚⠁⠀
⠀⠀⠀⠀⠀⠀⠀⡟⠀⣾⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⣿⣿⣿⣶⣦⣤⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣁⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠁⢾⣿⣦⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⣳⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣻⣿⣿⢿⣿⣿⣿⣿⣿⣿⡿⢡⣿⣿⣯⣻⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠙⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⢀⣿⣿⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⣾⣿⣿⣿⣿⠏⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠠⣾⡿⠏⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡏⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⠁⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣧⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⡀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣧⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠋⢀⡟⣿⣧⠀⢻⣦⠀⠀⠾⢿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠋⠙⣿⣿⡏⠀⠀⠀⠀⠀⠀⢠⡿⠻⣿⣿⠇⢠⠟⠀⣿⡟⠀⠀⠙⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⠟⣻⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠄⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⢺⡇⢠⣿⡏⢠⣧⣤⣶⣿⠀⠀⠀⠀⠀⠲⣿⡿⠿⠿⠿⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣾⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠘⢧⣾⣿⠃⢿⣿⢁⣨⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡾⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿⣦⣤⣶⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⠎⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠸⠛⣿⣯⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡠⢫⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠻⠿⠯⠿⠟⠋⠀"""

    print(bull)
    continueApp = 'y'
    while continueApp == 'y':
        print("---------------------------WELCOME TO MATADOR BANKING---------------------------")
        print("1. Login as Employee:")
        print("2. Login as Customer:")
        valid = False
        option = 0
        while not valid:
            try:
                option = int(input())
                if option == 1 or option == 2:
                    valid = True
                else:
                    print("Please enter a valid option")
            except ValueError:
                print("Please enter a valid option")

        match option:
            case 1:
                print("Please enter Employee email")
                email = str(input())

                print("Please enter Employee password")
                password = str(input())
                try:
                    acc = loginService.employeeLogin(email, password)
                    if acc is None:
                        print("Invalid Login, Please try again")
                        continue
                    else:
                        print("Login Successful")
                except AttributeError:
                    print("Account does not exist")
                print("Welcome", acc.getFirstName(), acc.getLastName())
                empMenu = 'y'
                while empMenu == 'y':
                    valid = False
                    empOpt = 0
                    print("1. Create New Customer Account")
                    print("2. View All Accounts")
                    print("3. Exit")
                    while not valid:
                        try:
                            empOpt = int(input())
                            if empOpt < 0 or empOpt > 3:
                                print("Please enter a valid option")
                            else:
                                valid = True
                        except ValueError:
                            print("Please enter a valid option")
                    match empOpt:
                        case 1:
                            valid = False
                            while not valid:
                                print("Please enter customer first name")
                                firstName = input()
                                if firstName.isalpha() and len(firstName) > 0:
                                    valid = True
                                else:
                                    print("Please enter a valid name")
                            valid = False
                            while not valid:
                                print("Please enter customer last name")
                                lastName = input()
                                if lastName.isalpha() and len(lastName) > 0:
                                    valid = True
                                else:
                                    print("Please enter a valid name")
                            valid = False
                            while not valid:
                                # I can do validation here, check to see if the inputted string contains the character '@'
                                print("Please enter customer email")
                                cusEmail = input()
                                if len(cusEmail) > 0:
                                    valid = True
                                else:
                                    print("Please enter valid email")
                            valid = False
                            while not valid:
                                print("Please enter employee password")
                                cusPass = input()
                                # Also can do more validation here, check if is alpha numeric, and maybe goes beyond a certain length
                                if len(cusPass) > 0:
                                    valid = True
                                else:
                                    print("Please enter valid password")
                            accountService.createAccount(firstName, lastName, cusEmail, cusPass)
                            print("account successfully created")

                        case 2:
                            print("All customer accounts:")
                            list = accountService.viewAllAccounts()
                            print("{:<16} {:<12} {:<30} {:<10} {:<10}".format("First", "Last", "Email", "Balance", "Account ID"))
                            for obj in list:
                                print("{:<16} {:<12} {:<30} {:<10} {:<10}".format(
                                    obj.getFirstName(), obj.getLastName(), obj.getEmail(), obj.getAccountBalance(), obj.getCustomerId()))

                        case 3:
                            print("Thank you for using Matador Banking")
                            sys.exit()
                    print("Would you like to do something else? y/n")
                    valid = False
                    while not valid:
                        empMenu = input().lower()
                        if empMenu == 'n':
                            print("Thank you for using Matador Banking")
                            sys.exit()
                        elif empMenu == 'y':
                            break
                        else:
                            print("Please enter y or n")

            case 2:
                print("Please enter customer email")
                email = str(input())
                print("Please enter customer password")
                password = str(input())
                acc = loginService.customerLogin(email, password)
                if acc is None:
                    print("Invalid Login, please try again")
                    continue
                else:
                    print("Login Successful")
                print("Welcome", acc.getFirstName(), acc.getLastName())
                customerMenu = 'y'
                while customerMenu == 'y':
                    option = 0
                    valid = False
                    print("1. View Account Details")
                    print("2. Transfer Money")
                    print("3. View transaction history")
                    print("4. Logout")
                    while not valid:
                        try:
                            option = int(input())
                            if option > 4 or option < 1:
                                print("Please enter a valid option")
                            else:
                                valid = True
                        except ValueError:
                            print("Please enter a valid option")

                    match option:
                        case 1:
                            accDetails = accountService.viewAccountDetails(acc.getId())
                            print("{:<16} {:<16} {:<10}".format("Name", "Balance", "Email"))
                            print("{:<16} {:<16} {:<10}".format(f"{accDetails.getFirstName()} {accDetails.getLastName()}", accDetails.getAccountBalance(), accDetails.getEmail()))
                        case 2:
                            transferOpt = 0
                            print("Please enter an option")
                            print("1. Deposit Money")
                            print("2. Withdraw Money")
                            print("3. Send Money")
                            valid = False
                            while not valid:
                                try:
                                    transferOpt = int(input())
                                    if transferOpt < 0 or transferOpt > 3:
                                        print("Please enter a valid option")
                                    else:
                                        valid = True
                                except ValueError:
                                    print("Please enter a valid option")
                            match transferOpt:
                                case 1:
                                    print("Please enter the amount you would like to deposit")
                                    valid = False
                                    while not valid:
                                        try:
                                            depo = int(input())
                                            if depo <= 0:
                                                print("Please enter a valid amount to deposit")
                                            else:
                                                accountService.deposit(acc.getId(), depo)
                                                valid = True
                                        except ValueError:
                                            print("Please enter a valid amount to deposit")
                                case 2:
                                    print("Please enter the amount you would like to withdraw")
                                    valid = False
                                    while not valid:
                                        try:
                                            withdraw = int(input())
                                            if withdraw <= 0:
                                                print("Please enter a valid amount to withdraw")
                                            else:
                                                accountService.withdraw(acc.getId(), withdraw)
                                                valid = True
                                        except ValueError:
                                            print("Please enter a valid amount to withdraw")
                                case 3:
                                    print("Please enter the email of the recipient you would like to send to ")
                                    others = input()
                                    print("Please enter the amount of money you would wish to send:")
                                    money = 0
                                    valid = False
                                    while not valid:
                                        try:
                                            money = int(input())
                                            valid = True
                                            accountService.sendMoney(others, money, acc.getId())
                                        except ValueError:
                                            print("Please enter a valid amount")
                        case 3:
                            print("----------Present transaction history for", acc.getFirstName(), acc.getLastName(), "----------")
                            allTransactions = accountService.viewTransactionHistory(acc.getId())
                            print("Date \t\t\t Type \t\t  Amount \t\t\t   Id Number")
                            for transaction in allTransactions:
                                print("{:<16} {:<12} {:<20} {:<10}".format(transaction.getDate(), transaction.getTransactionType(), transaction.getAmount(), transaction.getIdNumber()))

                        case 4:
                            print("Thank you for using Matador Banking")
                            sys.exit()

                    print("Would you like to do something else? y/n")
                    valid = False
                    while not valid:
                        customerMenu = input().lower()
                        if customerMenu == 'n':
                            print("Thank you for using Matador Banking")
                            sys.exit()
                        elif customerMenu == 'y':
                            break
                        else:
                            print("Please enter y or n")


main()
