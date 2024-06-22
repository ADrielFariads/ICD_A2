from bs4 import BeautifulSoup
import requests

# Funcao que coleta os comentarios
def getWeb(url, comments):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    divContent = soup.find_all("div", class_="content")

    for content_div in divContent:
        i = 0
        text_div = content_div.find("div", class_="text show-more__control")
        if text_div:
            comments.insert(i, text_div.text.strip())
            i += 1
    
    return comments