import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

movies = soup.find_all(name="h3", class_="title")

top_100_movies = []

for movie in movies:
    m = movie.getText()
    top_100_movies.append(m)

top_100_movies.reverse()

# Jezeli uzyjemy encoding to nie bedzie bledu UnicodeEncodeError
with open("movies.txt", "a", encoding="utf-8") as file:
    for movie in top_100_movies:
        file.write(movie)
        file.write("\n")
