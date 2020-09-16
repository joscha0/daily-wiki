import os
from flask import Flask, render_template, request, redirect, jsonify, abort
import requests
import db
import re

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/confirm/<email>')
def confirm(email):
    if(db.validateuser(email)):
        return render_template('subscribed.html')
    else:
        text = 'Email does not exist.'
        return render_template('error.html', text=text, again=True)


@app.route('/unsubscribe/<email>')
def unsubscribe(email):
    if(db.deluser(email)):
        return render_template('unsubscribed.html')
    else:
        text = 'You are not subscribed to this newsletter.'
        return render_template('error.html', text=text, again=False)


@app.route('/users')
def getusers():
    return jsonify(db.getusers())


@app.route('/deluser/<email>/<token>')
def deluser(email, token):
    if(db.deluser(email)):
        return "Deleted User"
    else:
        return "User doesn't Exist"


def verify(email):
    return re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.form
    email = data['email'].strip()
    language = data['lang'].strip()
    if(not verify(email)):
        text = "Invalid Email"

    elif(db.adduser(email, language)):
        text = f' Please click on the link in the email I sent to {email}, to confirm your registration!'

    else:
        text = 'User Already Exists'
    return render_template('index.html', message=text)


if __name__ == '__main__':
    app.run(debug=True)
