import pandas as pd
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

df = pd.read_csv('urlList.csv')
df = df[['url']]
df.head()

def get_description(soup):
    if soup.findAll("meta", attrs={"name": "description"}):
        return soup.find("meta", attrs={"name": "description"}).get("content")
    else:
        return

def get_keywords(soup):
    if soup.findAll("meta", attrs={"name": "keywords"}):
        return soup.find("meta", attrs={"name": "keywords"}).get("content")
    else:
        return

def get_title(soup):
    if soup.findAll("title"):
        return soup.find("title").string
    else:
        return

// main function start here
df_pages = pd.DataFrame(columns = ['url', 'title', 'description', 'keywords'])
for index, row in df.iterrows(): 
    url = row['url']
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 
                            'html.parser', 
                            from_encoding=response.info().get_param('charset'))

    title = get_title(soup)
    description = get_description(soup)
    keywords = get_keywords(soup)

    page = {
        'url': row['url'],
        'title': title,
        'description': description,
        'keywords': keywords
    }

    df_pages = df_pages.append(page, ignore_index=True)

df_pages.to_csv('scrapedMeta.csv')  
