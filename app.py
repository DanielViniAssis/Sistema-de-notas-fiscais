from flask import Flask, render_template, request, redirect, url_for, flash
from peewee import DoesNotExist
import bcrypt
import secrets
import logging
from config import configure_all

app = Flask(__name__)

app.secret_key = "super secret key"

configure_all(app)

@app.route("/")
def home():
    return render_template("login_page.html")

if __name__ == '__main__':
    app.run(debug=True)

