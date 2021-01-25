import twitter
import os
from getwiki import get_wiki_for_twitter

api = twitter.Api(consumer_key=os.environ['consumer_key'],
                  consumer_secret=os.environ['consumer_secret'],
                  access_token_key=os.environ['access_token_key'],
                  access_token_secret=os.environ['access_token_secret'])

try:
    text, link, img_url = get_wiki_for_twitter()
except:
    print(f"Error getting article for en")

post = text[:276-len(link)]+'... '+link

api.PostUpdate(status=post, media=img_url)
