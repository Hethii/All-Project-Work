import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
# print(soup)

title = soup.find_all("h3")

movie_name = [name.getText() for name in title]

# print(movie_name)

# This apart from the inbuilt reversed feature also turn the list around:
movies = movie_name[::-1]
# print(movies)

with open("movies.txt", "w") as file:
    for name in reversed(movie_name):
        # print(name)
        new_name = name.encode("utf8")
        # file.write(f"{new_name}\n")
