Welcome to Matador Banking Application
Here are a list of steps to ensure you are able to run the application.
-Ensure you have the latest version of SQLite3 installed.

-After installing the repository change the file path of ALL SQL queries in the login
and accountDAO files to your local root path of the downloaded location.
It will not run until you fix this.


-After installing the repo, delete the flag.txt from your venv folder, and run initalizeDB.py
this will create the database in your local machine.
-From then, run presentationlayer.py, and you will be able to access the application.

Use one of the admin credentials to login as employee, then create your customer accounts:
1. email: emp 				password: emp
2. email: admin@matadorbanking.com 	password: admin1

*If you want to create new employee inserts into the table, you can do so with a third party AP via tablesplus,
or you can simply change the SQL script, and reinitalize the database. Another way
is writing your own create employee queries in the accountDAO.



