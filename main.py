from web import getWeb
from openia import addInfo


# Dicionario que contem o codigo especifico de um url para cada filme
urls = {
    "Saving Private Ryan": "tt0120815",
    "Jaws": "tt0073195",
    "Schindler's List": "tt0108052",
    "Raiders of the Lost Ark": "tt0082971",
    "E.T. the Extra-Terrestrial": "tt0083866",
    "The Fabelmans": "tt14208870",
    "Marcus Mumford: Cannibal":"tt21318180",
    "Ready Player One":"tt1677720",
    "The BFG":"tt3691740",
    "War Horse":"tt1568911"
}

# Dicionario que contem os comntarios
comments = {
    "Saving Private Ryan": [],
    "Jaws": [],
    "Schindler's List": [],
    "Raiders of the Lost Ark": [],
    "E.T. the Extra-Terrestrial": [],
    "The Fabelmans": [],
    "Marcus Mumford: Cannibal": [],
    "Ready Player One": [],
    "The BFG": [],
    "War Horse": []

}

# Funcao que coleta os comentarios
for url, url_Id in urls.items():
    getWeb(f"https://www.imdb.com/title/{url_Id}/reviews/?ref_=tt_ql_2", comments[url])
    addInfo(comments[url], url)