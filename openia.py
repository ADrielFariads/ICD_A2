from openai import OpenAI
import re

# INSERIR A CHAVE AQUI
key = "sk-proj-JfeivvuWXmM2A7rHBnLiT3BlbkFJBqnVUNyrdvyWnErHVaED"

 # Função que pede aspectos positivos do comentario para a api openai
def get_positive_aspects(comment):
    prompt = [{"role": "user",
               "content": f"A seguir, você receberá um comentário referente a um filme. Cite os aspectos positivos sobre o filme presentes no comentário. Se não houver aspectos positivos, me retorne um espaço vazio. Me retorne apenas os aspectos principais resumidos em um único parágrafo. O comentário é: {comment}"}]
    client = OpenAI(api_key = key)

    response = client.chat.completions.create(
        messages= prompt,
        model= "gpt-3.5-turbo-0125",
        max_tokens= 4000,
        temperature= 0
    )
    return response.choices[0].message.content

# Função que pede aspectos negativos do comentario para a api openai
def get_negative_aspects(comment):
    prompt = [{"role": "user",
               "content": f"A seguir, você receberá um comentário referente a um filme. Cite os aspectos negativos sobre o filme presentes no comentário. Se não houver aspectos negativos, me retorne um espaço vazio. Me retorne apenas os aspectos principais resumidos em um único parágrafo. O comentário é: {comment}"}]
    client = OpenAI(api_key = key)

    response = client.chat.completions.create(
        messages= prompt,
        model= "gpt-3.5-turbo-0125",
        max_tokens= 4000,
        temperature= 0
    )
    return response.choices[0].message.content

# Função que coleta os aspectos mais relevantes para a openai
def get_resume(lista, letter):
    quality = ""
    if letter == "p":
        quality = "positivos"
    if letter == "n":
        quality = "negativos"
    prompt = [{"role": "user",
               "content": f"A seguir, você receberá uma lista contendo aspectos {quality} de um filme. Resuma essa lista, remova duplicatas e retorne apenas os três aspectos mais destacados em três tópicos que iniciam com - e terminam com um ponto final. A lista é: {lista}"}]
    client = OpenAI(api_key = key)

    response = client.chat.completions.create(
        messages= prompt,
        model= "gpt-3.5-turbo-0125",
        max_tokens= 4000,
        temperature= 0
    )
    return response.choices[0].message.content

# Funcao que trata o texto voltado pela openai
def resume_treatment(resume):
    resume = re.sub("\n", "", resume)
    resume = re.sub("-", "", resume)

    return resume

def get_genre(movie):
    prompt = [{"role": "user",
               "content": f"A seguir, você receberá o nome de um filme. Quero que você me responda apenas o gênero desse filme, iniciado com letra maiúscula e sem ponto ponto final. O nome do filme é: {movie}"}]
    client = OpenAI(api_key = key)

    response = client.chat.completions.create(
        messages= prompt,
        model= "gpt-3.5-turbo-0125",
        max_tokens= 4000,
        temperature= 0
    )
    return response.choices[0].message.content