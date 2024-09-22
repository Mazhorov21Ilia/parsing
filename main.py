import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

ua = UserAgent()
fake_ua = {'user-agent': ua.random}


# def find_email(link):
#     try:
#         response = requests.get(url=link.strip(), headers=fake_ua)
#         soup = BeautifulSoup(response.content, "html.parser")
#         email = re.findall(
#             "[a-z]+@[\w\d-]+.[a-z]+", soup.text)
#         if email:
#             return email[0].strip()
#             # res.append(f"{link.strip()} - {email[0].strip()}\n")
#             # print(f"{link.strip()} - {email[0].strip()}")
#     except Exception as e:
#         return "Error"


# def find_site(html):
#     soup = BeautifulSoup(html.content, "html.parser")
#     site_link = soup.find("section", "page-section-compact company-basics").find("a",
#                                                                                  attrs={"data-link-override": "website"})["href"]
#     with open("result.txt", "a", encoding="utf-8") as file:
#         email = find_email(site_link)
#         file.write(f"{site_link} - {email}\n")


# def find_agent(html):
#     soup = BeautifulSoup(html.content, "html.parser").find_all(
#         "section", "page-section-compact archive-item")
#     for agent in soup:
#         link = agent.find("a", "btn mt-btn d-block")["href"]
#         find_site(requests.get(url=link))


# for i in range(1, 7):
#     html_doc = requests.get(
#         url=f"https://marketing-tech.ru/company_tags/analytics/page/{i}/")
#     html_doc.encoding = "utf-8"
#     find_agent(html_doc)

response = requests.get(
    url="https://makodigital.ru/?utm_source=marketing-tech&utm_medium=referral_&utm_campaign=kartochka", headers=fake_ua)
soup = BeautifulSoup(response.content, "html.parser")
print(re.findall("[a-z]+@[\w\d-]+.[a-z]+", response.text))
print(response.text)
