
''' Alternate method no. 2. Works with HTML-file wheresMarianne.html.
Scraping latest tweet from the Twitter Account MarianneKontor with time stamp. '''

from flask import Flask
from flask import request
from flask import render_template
#import stringComparison
from scrape-twitter import Scraping

app = Flask(__name__)

@app.route('/')
def my_site():
    return render_template("wheresMarianne.html")

    #@app.route('/', methods=['POST'])
    #def my_site_post():
    #flavor_text = request.form['Marianne: ']
    #tweet = request.form[]
    #timestamp = request.form['text2']
    #plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)
    #if plagiarismPercent > 50 :
    #    return "<h1>Plagiarism Detected !</h1>"
    #else :
    #    return "<h1>No Plagiarism Detected !</h1>"
    return Scraping().scrape(0)

if __name__ == '__main__':
    app.run()



      
            page = requests.get('https://twitter.com/MarianneKontor')
            tree = html.fromstring(page.content)

            tweets = tree.xpath('//p[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()')
            timestamp = tree.xpath('//span[@class="_timestamp js-short-timestamp js-relative-timestamp"]/text()')

            tweet = 'Marianne: ' + str(tweets[0]) + ', for ' + str(timestamp[0]) + ' siden'

            return tweet, timestamp