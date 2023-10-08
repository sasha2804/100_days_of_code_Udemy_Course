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
movies_titles.reverse()

print(type(movies_titles[0]))


file = open('45_day_Parsing_HTML_Making_Soup/2_project/movies_list.txt', 'w')

with open ('45_day_Parsing_HTML_Making_Soup/2_project/movies_list.txt', 'w') as file:

    for item in movies_titles:
        file.write(item + '\n')
    file.close()



# for item in movies_titles:
#     file.write(item + '\n')
# file.close()





