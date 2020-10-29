<h1 align="center">Daily Wiki Newsletter</h1>
<p align="center">
  A simple flask app that handles the sign up to a newsletter with double opt-in function.
</p>
<p align="center">
  <img alt="Website" src="https://img.shields.io/website?label=demo&up_message=online&url=https%3A%2F%2Fdaily-wiki-newsletter.herokuapp.com%2F">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/joscha0/daily-wiki">
  <img alt="GitHub" src="https://img.shields.io/github/license/joscha0/daily-wiki">
</p>
<p align="center">
  Demo: https://daily-wiki-newsletter.herokuapp.com/
</p>

### 1. Signup
Users can signup with their email adress and select the language of the wikipedia article of the day.

<img src="https://i.postimg.cc/MK8MRxXB/signup.png" width=300>

### 2. Email confirmation
After they have confirmed their email, they are subscribed to the newsletter.

<img src="https://i.postimg.cc/gk9SZwvK/image.png" width=300>

<img src="https://i.postimg.cc/mk70H7k0/image.png" width=300>

### 3. Send Email

A daily cron job will run `sendmail.py`. This will scrape the wikipedia article of the day in the selected language to the email list in Firebase.

## Firebase
The Cloud Firestore Data Structure for the emails:

![firebase.png](https://i.postimg.cc/RhnnQZzr/firebase.png)
