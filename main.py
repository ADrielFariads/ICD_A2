# encoding: utf-8
'''
Módulo principal do projeto.
Execução: Após realizar a coleta de informações de filmes disponíveis no site "https://www.imdb.com",
cria um arquivo csv com análise feita a partir da API OpenAI dos comentários do público referente a
filmes recentes dirigidos por Steven Spielberg.

'''
import web as wb
import openailocal as opai
from data import *
import pandas as pd

titles = ["Filme", "Ano", "Gênero", "Avaliação Média", "Porcentagem de Aprovações", "Aspectos Positivos", "Aspectos Negativos"]
data_base = []

for movie, code in urls.items(): # Cada filme tem um codigo que muda na url
    url = f"https://www.imdb.com/title/{code}/reviews/?ref_=tt_ql_2"
    comments_base = wb.get_web(url, comments[movie]) # Para cada link, a funcao pega todos os comentarios e adiciona a uma lista
    for comment in comments_base: # Para cada comentario, a funcao pede a openai retorne os aspectos do filme contidos nele
        positive_aspects[movie] += opai.get_positive_aspects(movie)
        negative_aspects[movie] += opai.get_negative_aspects(movie)

    positive_aspects[movie] = opai.resume_treatment(opai.get_resume(positive_aspects[movie], "p")) # Resume os aspectos positivos
    negative_aspects[movie] = opai.resume_treatment(opai.get_resume(negative_aspects[movie], "n")) # Resume os aspectos negativos
    
    line = []
    year = wb.get_movie_year(url)
    genre = opai.get_genre(movie)
    rate = wb.get_rate(url)
    approval = wb.get_approvals(url)
    line += [movie, year, genre, rate, approval, positive_aspects[movie], negative_aspects[movie]] # Aqui faz linha por linha e adiciona a tabela
    data_base.append(line)

df = pd.DataFrame(data = data_base, columns = titles)
df.to_csv("steven_spielberg's_movies_century_21.csv", index = False, encoding = "utf-8-sig")
