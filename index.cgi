

#!/usr/bin/python   
print('Content-type: text/html\r\n\r')
from lxml import html
import requests


class Functions():
        def __init__(self):
            return None
        def scrape_latest_tweet(self):
            ''' Scraping latest tweet from 
                the Twitter Account MarianneKontor with time stamp. '''      
            page = requests.get('https://twitter.com/MarianneKontor')
            tree = html.fromstring(page.content)

            tweets = tree.xpath('//p[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()')
            timestamp = tree.xpath('//span[@class="_timestamp js-short-timestamp js-relative-timestamp"]/text()')

            tweet = 'Marianne: ' + str(tweets[0]) + ', for ' + str(timestamp[0]) + ' siden'

            return tweet

print Functions().scrape_latest_tweet()