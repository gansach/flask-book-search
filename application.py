import os

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():    
    return redirect("/search")

@app.route("/search", methods = ["GET", "POST"])
def search():
    # User reached route via POST
    if request.method == "POST":
        return render_template("searched.html")
    
    # User reached route via GET
    else:
        return render_template("search.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        return render_template("error.html", error = "TODO Post register")
    else:
        return render_template("register.html")

@app.route("/api/<int:isbn>")
def book_json(isbn):
    return render_template("error.html", error = "TODO json app")