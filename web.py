from bs4 import BeautifulSoup
from math import ceil
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

# Funcao que coleta a media da avaliacao
def get_rates(url):
    # Define a base de busca:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    rates_base = soup.find_all("span", class_="rating-other-user-rating")

    # Coleta todas avaliacoes no formato X/1O:
    rates = []
    for rate in rates_base:  
        rate = rate.text.strip()
        rates.append(rate)

    # Calcula a media de todas as avaliacoes:
    rates_sum = 0
    for rate in rates:
        rate = rate.split("/") # X/10 vira ["X", "10"]
        rates_sum += int(rate[0])/len(rates)

    rates_sum = ceil((rates_sum*10))/10 # ceil: funcao teto. Calcula a aproximacao de um decimal

    return rates_sum