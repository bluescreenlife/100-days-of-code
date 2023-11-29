import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_list = []

movies = soup.find_all("h3", class_="title")
for movie in movies:
    movie_list.append(movie.get_text())

def get_number(item):
    try:
        return int(item.split(")")[0])
    except ValueError:
        return int(item.split(":")[0])


movie_list.sort(key=get_number)

with open("./top_movies.txt", "w") as file:
    for _ in movie_list:
        file.write(f"{_}\n")