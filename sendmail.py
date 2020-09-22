from email.mime.text import MIMEText
import smtplib

from db import firestore
import os

from getwiki import get_wiki


def send_email(img, text, email):
    unsubscribe_tag = f'<a href="https://daily-wiki-newsletter.herokuapp.com/unsubscribe/{email}">unsubscribe</a>'

    msg = MIMEText(str(img) + 3*'<br>' + text + 3 *
                   '<br>' + unsubscribe_tag, 'html')
    msg['Subject'] = 'today wiki'
    msg['From'] = 'daily-wiki@960.eu'
    msg['To'] = email

    s = smtplib.SMTP_SSL(os.environ['host'], 465)
    s.login(os.environ['username'], os.environ['password'])
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


def send_confirm_email(email):
    confirm_tag = f'<a href="https://daily-wiki-newsletter.herokuapp.com/confirm/{email}">confirm email</a>'

    text = f'Confirm your Email: <br> {confirm_tag}'

    msg = MIMEText(text, 'html')
    msg['Subject'] = 'confirm daily wiki newsletter'
    msg['From'] = 'daily-wiki@960.eu'
    msg['To'] = email

    s = smtplib.SMTP_SSL(os.environ['host'], 465)
    s.login(os.environ['username'], os.environ['password'])
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


if __name__ == "__main__":
    languages = ["en", "de", "fr", "sv", "ja", "zh"]
    wikis = {}
    for language in languages:
        img, text = get_wiki(language)
        wikis[language] = (img, text)
    data = firestore.getusers()
    for email in data:
        img, text = wikis[data[email]["language"]]
        send_email(img, text, email)
