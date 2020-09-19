from email.mime.text import MIMEText
import smtplib
import sys
import requests
import bs4
from datetime import datetime
import json

import passwords


def get_wiki(language):
    date = datetime.now().strftime("%Y%m%d000000")

    link = f'https://{language}.wikipedia.org/wiki/Special:FeedItem/featured/{date}/{language}'
    res = requests.get(link)

    wiki = bs4.BeautifulSoup(res.text, "lxml")

    if language == "de":
        elems = wiki.select('.hauptseite-box-content')
        text = elems[0].getText()
    elif language == "fr":
        header = wiki.find_all('h2')[1]
        text = ""
        for tag in wiki.find("h1").next_siblings:
            if tag.name == "ul":
                break
            elif tag.name == "p":
                text += tag.getText()
        elems = wiki.select('p')
        text = elems[4].getText()
    else:
        elems = wiki.select('p')
        text = elems[0].getText()

    imgs = wiki.select('img')
    imglink = 'http:'+imgs[0]['src']
    img = imgs[0]
    img['src'] = 'http:'+img['src']

    return img, text


def send_email(img, text, email):
    unsubscribe_tag = f'<a href="http://daily-wiki.960.eu/unsubscribe/{email}">unsubscribe</a>'

    msg = MIMEText(str(img) + 3*'<br>' + text + 3 *
                   '<br>' + unsubscribe_tag, 'html')
    msg['Subject'] = 'today wiki'
    msg['From'] = 'daily-wiki@960.eu'
    msg['To'] = email

    s = smtplib.SMTP_SSL(passwords.host, 465)
    s.login(passwords.username, passwords.password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


def send_confirm_email(email):
    confirm_tag = f'<a href="http://daily-wiki.960.eu/confirm/{email}">confirm email</a>'

    text = f'Confirm your Email: <br> {confirm_tag}'

    msg = MIMEText(text, 'html')
    msg['Subject'] = 'confirm daily wiki newsletter'
    msg['From'] = 'daily-wiki@960.eu'
    msg['To'] = email

    s = smtplib.SMTP_SSL(passwords.host, 465)
    s.login(passwords.username, passwords.password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


if __name__ == "__main__":
    languages = ["en", "de", "fr", "sv", "ja", "zh"]
    wikis = {}
    for language in languages:
        img, text = get_wiki(language)
        wikis[language] = (img, text)
    print(wikis)
    with open("email.json", "r") as jsonFile:
        data = json.load(jsonFile)
    for email in data:
        img, text = wikis[data[email]["language"]]
        send_email(img, text, email)
