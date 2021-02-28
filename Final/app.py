import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, g
from flask_login LoginManager, UserMixin
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/workouts")
def workouts():
    return render_template("workouts.html")

@app.route("/mealplan")
def mealplan():
    return render_template("mealplan.html")

@app.route("/challenges")
def challenges():
    return render_template("challenges.html")

@app.route("/user")
def user():
    if session.get('logged_in'):
         return render_template("user.html")
    else:
         return redirect("login.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Log user in"""

#     # Forget any user_id
#     # session.clear()

#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":

#         # Query database for username
#         rows = db.execute("SELECT * FROM users WHERE email = :email", email=request.form.get("email"))

#         # Ensure username exists and password is correct
#         if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
#             error = 'Invalid username or password'
#             return redirect('login.html', error=error)

#         # Remember which user has logged in
#         session["user_id"] = rows[0]["id"]
#         session['logged_in'] = True

#         # Redirect user to home page
#         return redirect("/")

#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("login.html")


# @app.route("/logout")
# def logout():
#     """Log user out"""

#     # Forget any user_id
#     # session.clear()

#     session['logged_in'] = False

#     # Redirect user to login form
#     return redirect("/")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     """Register user for an account."""

#     # session.clear()

#     if request.method == "POST":

#         if not request.form.get("password") == request.form.get("confirmation"):
#             error = 'Passwords do not match'
#             return redirect('register.html', error=error)


#         # ar galima kaipnors svariau pachekint ar egzistuoja username?

#         usernamecheck = db.execute("SELECT * FROM users WHERE username = :username", username = request.form.get("username"))
#         if len(usernamecheck) == 1:
#             error = 'Username already exists'
#             return redirect('register.html', error=error)

#         emailcheck = db.execute("SELECT * FROM users WHERE email = :email", username = request.form.get("email"))
#         if len(usernamecheck) == 1:
#             error = 'Email already exists'
#             return redirect('register.html', error=error)

#         db.execute("INSERT INTO users (username, email, hash) VALUES (?,?,?)", request.form.get("username"), request.form.get("email"), generate_password_hash(request.form.get("password")))
#         #cia irgi ar galima kaipnors maziau messy padaryti? ar ir taip gerai?

#     else:
#          return render_template("register.html")

#     return redirect("login.html")