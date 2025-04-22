from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from peewee import DoesNotExist
from models.user import User
import bcrypt
import secrets
import logging  

login_route = Blueprint('login', __name__)

@login_route.route("/", methods=["GET", "POST"])
def login_register():
    if request.method == 'POST':
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        logging.debug(f"Email recebido: {email}")
        logging.debug(f"Password recebido: {password}")

        if not email or not password:
            flash('Todos os campos precisam ser preenchidos!!')
            return redirect(url_for('login.login_register'))
        try:
            user = User.get(User.email == email)
            logging.debug(f"Usuário encontrado: {user.email}")
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return redirect(url_for('invoice.form_invoice'))
            else:  
                flash('Senha ou E-mail incorreto!')
                return redirect(url_for('login.login_register'))
        except DoesNotExist:
            logging.debug("Usuário não encontrado no banco de dados!")
            flash("O usuário não existe!!!")
            return redirect(url_for('login.login_register'))
    return render_template("login_page.html")