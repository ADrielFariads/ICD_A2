import web as wb
import openia as opai
from data import *

for movie, url in urls.items():
    comments_base = wb.get_web(f"https://www.imdb.com/title/{url}/reviews/?ref_=tt_ql_2", comments[movie]) # Para cada link, a funcao pega todos os comentarios e adiciona a uma lista
    for comment in comments_base:
        positive_aspects[movie] = opai.get_positive_aspects(movie)
        negative_aspects[movie] = opai.get_negative_aspects(movie)
    positive_aspects[movie] = opai.get_resume(positive_aspects[movie], "p")
    negative_aspects[movie] = opai.get_resume(negative_aspects[movie], "n")
    print(positive_aspects[movie])
    print(opai.resume_treatment(positive_aspects[movie]))
    print()
    print(opai.resume_treatment(negative_aspects[movie]))
    print()
    
    if movie == "A.I. Artificial Intelligence":
        break