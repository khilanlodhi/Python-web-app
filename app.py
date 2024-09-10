from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="b199079722b4481b9566cfd191ae623f")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    articles = topheadlines['articles']

    news = []
    desc = []
    img = []

    for article in articles:
        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('index.html', context=mylist)

@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="b199079722b4481b9566cfd191ae623f")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']

    news = []
    desc = []
    img = []

    for article in articles:
        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('bbc.html', context=mylist)

if __name__ == "__main__":
    app.run(debug=True)
