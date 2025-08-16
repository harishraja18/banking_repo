# Version 4 => Banking Project

A simple web-based banking application built with Django.  
This version (v4) uses **PostgreSQL** as the backend database instead of SQLite and includes user authentication features such as registration, login, profile management, and password change.

---

## ✅ Features

- User Registration & Login
- Logout functionality
- Profile View and Edit
- Password Change with validation
- Messages for success/error feedback
- PostgreSQL database integration

---

## 🛠️ Requirements

| Package            | Version (recommended) |
|--------------------|------------------------|
| Python             | 3.13.x                  |
| Django             | 5.2.5                   |
| psycopg2-binary    | Latest                  |
| PostgreSQL         | 13+                     |

---

## ⚙️ Database Setup (PostgreSQL)

Create a database and user:

```sql
CREATE DATABASE banking_db;
CREATE USER banking_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE banking_db TO banking_user;

Add this in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'banking_db',
        'USER': 'banking_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Setup & Run Locally

# clone the repo
git clone https://github.com/harishraja18/banking_repo.git
cd banking_repo/Banking_project

# create and activate virtual environment
python -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt   # or install manually

# apply migrations
python manage.py migrate

# run the server
python manage.py runserver

-----------------------------------------------------------------------------------------------------------

## 🚀 Version 3 - Authentication & UI Update

*New Features:*
- User login and logout functionality.
- Profile page with user details after login.
- Bootstrap navbar for easy navigation.
- Integrated Bootstrap styling for better UI.

*How to Test:*
1. Register a new user via /register/ (if registration is enabled).
2. Login at /login/.
3. After login, you will be redirected to the profile page.
4. Use the navbar to logout.
