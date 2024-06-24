from openai import OpenAI
import re

# INSERIR A CHAVE AQUI
key = "sk-proj-nPKsllf0bXWAfNuXAiirT3BlbkFJGImCe9x0Zor5TiqxgFOX"

def get_positive_aspects(comment): # Função que pede aspectos positivos do comentario para a api openai
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

def get_negative_aspects(comment): # Função que pede aspectos negativos do comentario para a api openai
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

def get_resume(lista, letter): # Função que coleta os aspectos mais relevantes para a openai
    quality = ""
    if letter == "p":
        quality = "positivos"
    if letter == "n":
        quality = "negativos"
    prompt = [{"role": "user",
               "content": f"A seguir, você receberá uma lista contendo aspectos {quality} de um filme. Resuma essa lista, remova duplicatas e retorne apenas os três aspectos mais destacados em três tópicos que iniciem com -. A lista é: {lista}"}]
    client = OpenAI(api_key = key)

    response = client.chat.completions.create(
        messages= prompt,
        model= "gpt-3.5-turbo-0125",
        max_tokens= 4000,
        temperature= 0
    )
    return response.choices[0].message.content

def resume_treatment(resume):
    resume = re.sub("\n", "", resume)
    resume = re.sub("-", "", resume)

    return resume