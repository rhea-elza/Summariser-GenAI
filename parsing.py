import requests
from bs4 import BeautifulSoup
from summary import summarize
from newspaper import Article

def parser(app):
    summary_list = []
    try:
        #scrape the xml file
        r = requests.get(app)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        #extract text from article link 
        for item in articles[:10]:
            link = item.find('link').text
            article = Article(link, language="en")
            article.download()#To download the article
            article.parse()#To parse the article
            article_text = article.text
            article_summary = summarize(article_text)
            summary_list.append(article_summary)
        return summary_list
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)