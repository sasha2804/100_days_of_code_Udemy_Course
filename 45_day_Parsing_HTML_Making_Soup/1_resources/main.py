# from bs4 import BeautifulSoup
# # import lxml


# with open('45_day_Parsing_HTML_Making_Soup/1_resources/website.html',encoding="utf8") as my_file:
#     content = my_file.read()

# soup = BeautifulSoup(content, "html.parser")

# # print(soup.title.string)

# anchor_tags = soup.find_all(name='a')
# # print(anchor_tags)

# # for tag in anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

    

# heading = soup.find_all(name='h1', id='name')


# print(heading)

from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com')
yc_web_page = response.text
# print(yc_web_page)
soup = BeautifulSoup(yc_web_page, 'html.parser')
# # print(soup.title)
# anchor_tags = soup.find_all(name='a')
# print(anchor_tags)
# print(soup)
# article_tag = soup.find(name="a", class_="storylink")
# print(article_tag)
# print(article_tag)


