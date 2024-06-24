'''
Módulo auxiliar do projeto, responsável por realizar o webscrapping.
'''
import re
from bs4 import BeautifulSoup
from math import ceil
import requests

# Funcao que coleta os comentarios
def get_web(url, comments):
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

# Funcao que trata as avaliacoes
def rate_treatment(url):
    # Define a base de busca:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    rates_base = soup.find_all("span", class_="rating-other-user-rating")
    # Coleta todas avaliacoes no formato X/1O e adiciona a uma lista com inteiros:
    rates = []
    for rate in rates_base:  
        rate = rate.text.strip()
        rate = rate.split("/")
        rates.append(int(rate[0]))

    return rates

# Funcao que coleta a media da avaliacao
def get_rate(url):
    rates = rate_treatment(url)
    # Calcula a media de todas as avaliacoes:
    rates_sum = 0
    for rate in rates:
        rates_sum += rate/len(rates)
    rates_sum = ceil((rates_sum*10))/10 # ceil: funcao teto. Calcula a aproximacao de um decimal

    return rates_sum

# Funcao que coleta as aprovacoes
def get_approvals(url):
    # Define a base de busca:
    rates = rate_treatment(url)
    approved = 0
    for rate in rates:# Aprovado >= 8, Reprovado <=5
        if rate >= 8:
            approved += 1
        else:
            continue

    return approved

#Funcao que coleta o ano do filme
def get_movie_year(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    element = soup.find_all("span", class_="nobr")
    year = [i.text for i in element][0]
    year = re.sub(r"\s+", "", year)
    year = re.sub(r'[(){}[\]]', "", year)
    
    return year
