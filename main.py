from web import getWeb
from openia import addInfo, prompt

# Dicionario que contem o codigo especifico de um url para cada filme
urls = {
    "A.I. Artificial Intelligence": "tt0212720",
    "Minority Report": "tt0181689",
    "Catch Me If You Can" : "tt0264464",
    "The Terminal": "tt0362227",
    "War of the Worlds": "tt0407304",
    "Munich": "tt0408306",
    "Indiana Jones and the Kingdom of the Crystal Skull": "tt0367882",
    "The Adventures of Tintin": "tt0983193",
    "War Horse": "tt1568911",
    "Lincoln": "tt0443272",
    "Bridge of Spies": "tt3682448",
    "The BFG": "tt3691740",
    "The Post": "tt6294822",
    "Ready Player One": "tt1677720",
    "West Side Story": "tt3581652",
    "The Fabelmans": "tt14208870"
}

# Dicionario que contem os comntarios
comments = {
    "A.I. Artificial Intelligence": [],
    "Minority Report": [],
    "Catch Me If You Can" : [],
    "The Terminal": [],
    "War of the Worlds": [],
    "Munich": [],
    "Indiana Jones and the Kingdom of the Crystal Skull": [],
    "The Adventures of Tintin": [],
    "War Horse": [],
    "Lincoln": [],
    "Bridge of Spies": [],
    "The BFG": [],
    "The Post": [],
    "Ready Player One": [],
    "West Side Story": [],
    "The Fabelmans": []
}

# Funcao que coleta os comentarios
for url, url_Id in urls.items():
    getWeb(f"https://www.imdb.com/title/{url_Id}/reviews/?ref_=tt_ql_2", comments[url])
    addInfo(comments[url], url)