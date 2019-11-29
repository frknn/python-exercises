import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

films = soup.find_all("td", {"class": "titleColumn"})
ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

print(type(films))

rate = float(input("İstediğiniz oran: "))

for film, rating in zip(films, ratings):

    film = film.text
    rating = rating.text

    film = film.strip()
    film = film.replace("\n", "")

    rating = rating.strip()
    rating = rating.replace("\n", "")

    if float(rating) > rate:
        print(film, rating)
        print("**************************************************************")


