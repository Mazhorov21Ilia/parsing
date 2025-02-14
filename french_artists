import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
from tqdm import tqdm
from time import sleep
import re

url_s = "https://projets.cotemaison.fr"
ua = UserAgent()
fake_ua = {'user-agent': ua.random}
file_extensions = ['png', 'jpg', 'gif', 'jpeg', 'img', 'io', 'example']

def get_soup(link):
    response = requests.get(url=link, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def find_site(soup):
    site = soup.find(
        "div", class_="col col-right").find("a", class_="link")
    if site:
        site = url_s + site["href"]
        resp = requests.get(site, allow_redirects=False)
        return resp.headers["location"]
    else:
        return "Нет сайта"

def find_info(soup):
    infos = [i.text for i in soup.find(
        "div", class_="col-sub-mid col-sub-info").find_all("h4")]
    if len(infos) < 3:
        name = soup.find("div", class_="sub-col-name").find("h1").text
        infos.insert(0, name)
    return infos

def find_mail(link):
        res = []
        try:
            response = requests.get(link, headers=fake_ua, timeout=1)
        except:
            return "Нет подключения"
        
        emails = list(set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)))
        for email in emails:
            if not any(email.endswith(ext) for ext in file_extensions) and "wixpress" not in email:
                res.append(email)

        if res:
            return ", ".join(res)
        
        link = str(link + "contact") if link.endswith("/") else str(link + "/contact")
        try:
            response = requests.get(link, headers=fake_ua, timeout=1)
        except:
            return "Нет подключения"
        
        emails = list(set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)))
        for email in emails:
            if not any(email.endswith(ext) for ext in file_extensions) and "wixpress" not in email:
                res.append(email)
        if res:
            return ", ".join(res)
        return "Нет email"

if __name__ == "__main__":

    with open('res2.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Профиль", "Сайт", "Название", "Адрес", "Mail"])
        for i in tqdm(range(56, 58), ncols=80):
            main_soup = get_soup(
                f"https://projets.cotemaison.fr/recherche/pros?user_type=interiorarchitect&page={i}")
            for company in tqdm(main_soup.find_all("article", class_="listingPro listing-users-pro article-stamp is-not-brand"), ncols=80):

                try:
                    new_link = url_s + company.find("a")["href"]
                    soup = get_soup(new_link)
                    info = find_info(soup)
                    site = find_site(soup)
                    
                    mail = find_mail(site) if site != "Нет сайта" else "Нет email"
                    writer.writerow(
                        [new_link, site.strip(), info[0], info[-1], mail])
                except:
                    print(f"Ошибка подключения к {new_link}")
