# phonebook
Coding Temple Weekend Project #6

***

This is my sixth weekend project for Coding Temple. The assignment was to a **full-stack** web app using **Flask** along with various subsidiary frameworks: **SQLAlchemy**, **Alembic (Flask-Migrate)**, **SQLite**, and **Jinja**. I chose to style the frontend with **Bootstrap** to gain more familiarity with it. The program allows users to register; log in and out; and make, edit, and delete simple address book entries. User information, including the entries, is saved to a local database and is automatically retrieved on the next login, even if the program is closed. Users are only allowed to view and edit their own entries.

The challenge of this assignment was the coordination of a lot of moving parts across multiple files. In addition to the difficulties peculiar to Flask itself, the project involved the integration of all the skills we've learned so far in Coding Temple: html/css, Python, and database creation and management. I imagine that there will be little to distinguish my project from those of others in my cohort, since our main focus was technical, that is, on getting the app to run as intended. I did use **Pravatar** to assign random face images to each entry each time the program as run. This looks nice but would be of limited utility in a real use case since the photos are neither chosen by the user nor associated permanently with their entries. I also made a lot of use of the Bootstrap default colors to try to create a palette I enjoyed.

### prerequisites

This program requires python3 plus a number of python packages listed in requirements.txt. You can find instructions for installing them to a virtual environment below.

### installation
Here are the steps to take if you'd like to run my program:
1. Clone this repository.
2. Navigate to the 'phonebook' directory.
3. Create a virtual environment (not strictly necessary, but you may end up installing some unneeded Python packages to your system if you don't): ```python -m venv venv''' (Windows/Linux) or ```python3 -m venv venv``` (Mac).
4. Install the necessary packages: ```pip install -r requirements.txt```
5. Run the program: ```flask run```
6. Ctrl-click on ```http://127.0.0.1:5000```
7. You can close the program by closing your browser and pressing Ctrl-C in the terminal running it.

Thank you for your interest!
