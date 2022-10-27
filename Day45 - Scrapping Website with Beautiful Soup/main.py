from urllib import request
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")

# Uzyskanie tekstu z pierwszego linku na stronie
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article in articles:
    text = article.get_text()
    article_texts.append(text)

    link = article.find(name="a").get("href")
    article_links.append(link)

# W ten sposob uzyskamy tylko liczbe w formie int
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest = article_upvotes[0]

for score in article_upvotes:
    if score > largest:
        largest = score

largest_index = article_upvotes.index(largest)
print(largest_index)

# Musi byc +1 poniewaz upvotes jest 29 przez co inaczej jest odczytywany index / nie wszystkie linki maja upvotes
highets_title = article_texts[largest_index + 1]
highest_link = article_links[largest_index + 1]

print(highets_title)
print(highest_link)
