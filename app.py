import os
from flask import Flask, render_template, request, redirect, jsonify, abort
import requests
from db import firestore
import re
from sendmail import send_confirm_email

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/confirm/<email>')
def confirm(email):
    if(firestore.validateuser(email)):
        header = "Thanks for Subscribing!"
        text = "Your email has been confirmed. You'll receive your daily Wikipedia Mail from now on."
        return render_template('info.html', text=text, header=header)
    else:
        text = 'Email does not exist.'
        return render_template('info.html', text=text)


@app.route('/unsubscribe/<email>')
def unsubscribe(email):
    if(firestore.deluser(email)):
        header = "Sorry to see you go."
        text = "You have successfully unsubscribed from the newsletter."
        return render_template('info.html', text=text, header=header)
    else:
        text = 'You are not subscribed to this newsletter.'
        return render_template('info.html', text=text)


@app.route('/users')
def getusers():
    return jsonify(firestore.getusers())


@app.route('/deluser/<email>/<token>')
def deluser(email, token):
    if(firestore.deluser(email)):
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

    elif(firestore.adduser(email, language)):
        text = f' Please click on the link in the email that was sent to {email}, to confirm your registration!'
        send_confirm_email(email)
    else:
        text = 'User Already Exists'
    return render_template('index.html', message=text)


if __name__ == '__main__':
    app.run(debug=False)
