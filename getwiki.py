import requests
import bs4
from datetime import datetime


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