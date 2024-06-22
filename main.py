from web import getWeb
from openia import addInfo, prompt


# Dicionario que contem o codigo especifico de um url para cada filme
urls = {
    "Saving Private Ryan": "tt0120815",
    "Jaws": "tt0073195",
    "Schindler's List": "tt0108052"
}

# Dicionario que contem os comntarios
comments = {
    "Saving Private Ryan": [],
    "Jaws": [],
    "Schindler's List": []
}

# Funcao que coleta os comentarios
for url, url_Id in urls.items():
    getWeb(f"https://www.imdb.com/title/{url_Id}/reviews/?ref_=tt_ql_2", comments[url])
    addInfo(comments[url], url)