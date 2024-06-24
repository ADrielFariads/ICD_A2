import web as wb
import openia as opai
from data import *

lista_teste = []

for movie, code in urls.items(): # Cada filme tem um codigo que muda na url
    url = f"https://www.imdb.com/title/{code}/reviews/?ref_=tt_ql_2"
    comments_base = wb.get_web(url, comments[movie]) # Para cada link, a funcao pega todos os comentarios e adiciona a uma lista
    for comment in comments_base: # Para cada comentario, a funcao pede a openai retorne os aspectos do filme contidos nele
        positive_aspects[movie] += opai.get_positive_aspects(movie)
        negative_aspects[movie] += opai.get_negative_aspects(movie)

    positive_aspects[movie] = opai.resume_treatment(opai.get_resume(positive_aspects[movie], "p"))
    negative_aspects[movie] = opai.resume_treatment(opai.get_resume(negative_aspects[movie], "n"))
    linha = []
    print(positive_aspects[movie])
    print(opai.resume_treatment(positive_aspects[movie]))
    print()
    print(opai.resume_treatment(negative_aspects[movie]))
    print()
    year = wb.get_movie_year(url)
    rate = wb.get_rate(url)
    approval = wb.get_approvals(url)
    linha += [movie, year, approval, positive_aspects[movie], negative_aspects[movie]]
    lista_teste.append(linha)
    print(lista_teste)

    if movie == "A.I. Artificial Intelligence":
        break
