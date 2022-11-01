from bs4 import BeautifulSoup
import requests
from lxml import html

headers = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
 
url = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc'
 
page = requests.get(url)
tree = html.fromstring(page.content)
titles = tree.xpath('//*[@id="main"]/div/div[3]/div//h3/a/text()')
runtime = tree.xpath('//*[@id="main"]/div/div[3]/div//p[1]/span[3]/text()')
res = {titles[i]: runtime[i] for i in range(len(titles))}
print(res)