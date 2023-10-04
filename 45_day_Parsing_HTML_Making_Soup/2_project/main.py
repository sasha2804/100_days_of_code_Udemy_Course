import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



# Write your code below this line 👇
response = requests.get(URL)
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, 'html.parser')

# print(soup.prettify())

# print(soup.li)

movies_list = soup.find_all(name = 'h3',class_='title')

movies_titles = [movie.getText() for movie in movies_list]

print(movies_titles)
