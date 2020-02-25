Install Flask over PowerShell,CMD ect...

">mkdir flask-app
 >cd flask-app
 >py -m venv venv
 >venv\Scripts\activate
 >pip install Flask"

Open folder flask-app in IDE(Visual Studio Code...)

Run usersDB.py file in Visual Studio Code to set up database and tables
Run data.py file in Visual Studio Code to start application

Copy paste given url in terminal(example:http://127.0.0.1:5000/ ) in browser or
(CTRL+RIGHT MOUSE CLICK) on link given in terminal.

About app:
On login page is field username and password field, when you enter text
and click submit it redirect you to a page where are 4 links.
First link leads you to a form where you can add new user data and submit it
to a users table which is stored automatically in SQLite3 database table users.
Second link leads you to a page where you can view table users and stored data.
Third link is delete user link
Fourth link is showing table saves data.Table saves collects data from username field and
password field and stores their combinations in saves table.
