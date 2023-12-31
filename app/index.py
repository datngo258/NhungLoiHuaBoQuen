from flask import render_template, request, redirect
from sqlalchemy import join
import dao
from flask import flash

from app import app,login
import os
import hashlib
from app.admin import  *
import  utils
from flask_login import  login_user
@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/login_dinhdat",methods=['post'])
def login_dinhdat():
    username = request.form.get('username')
    password = request.form.get('password')

    user = utils.check_login(username=username, password=password)
    user = utils.check_login(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin/')

@login.user_loader
def load_user(user_id):
    return utils.get_user_by_id(user_id=user_id)





if __name__ == '__main__':
    from app import admin
    app.run(debug=True)