
''' Version 1.
    Scraping latest tweet from the Twitter Account 
    MarianneKontor with time stamp. '''

#from lxml import html
#import requests
import pyjs

class Scraping():
        def __init__(self):
            return None
        def scrape(self, N):
            ''' Scraping N latest tweet (0 is THE latest) from 
                the Twitter Account MarianneKontor with time stamp. '''      
            page = requests.get('https://twitter.com/MarianneKontor')
            tree = html.fromstring(page.content)

            tweets = tree.xpath('//p[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()')
            timestamp = tree.xpath('//span[@class="_timestamp js-short-timestamp js-relative-timestamp"]/text()')

            #tweet = 'Marianne: ' + str(tweets[0]) + ', for ' + str(timestamp[0]) + ' siden'
            return tweets[N], timestamp[N]

print Functions().scrape()
