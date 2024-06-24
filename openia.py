from openai import OpenAI

# INSERIR A CHAVE AQUI
key = ""

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