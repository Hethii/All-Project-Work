from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
# article_tag = soup.find(name="span", class_="titleline")
# # print(article_tag)
# article_text = article_tag.getText()
# # print(article_text)
# article_link_sort = article_tag.findAll('a')
# article_link = article_link_sort[0].get("href")
# print(article_link)
# article_score = soup.find(name="span", id="score_36957678").getText()
# # print(article_score)

article_text = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    article_link_sort = article_tag.findAll('a')
    link = article_link_sort[0].get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# article_upvotes.append(0)
# print(len(article_text))
# print(len(article_links))
# print(article_upvotes)

highest = max(article_upvotes)

highest_index = article_upvotes.index(highest)
print(highest)
add_to_highest = highest_index + 1
print(article_text[add_to_highest])
print(article_links[add_to_highest])



























# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
#
# # to get all tags:
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tags in all_anchor_tags:
#     # print(tags.getText())
#     # to get the links alone
#     # print(tags.get("href"))
#     pass
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# # print(section_heading.getText())
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# # print(company_url)
# # name = soup.select_one("#name")
# # print(name)
# #
# # headings = soup.select(".heading")
# # print(headings)
#
#
