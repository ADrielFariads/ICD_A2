from openai import OpenAI

def addInfo(coment): #função que pede insights para a api openai
    prompt = [{"role": "user",
               "content": f"A seguir, voce receberá um comentário referente a um filme. Classifique a opinião do usuário e diga em que aspectos o filme poderia melhorar.filme: saving prite ryan, {coment}"}]
    client = OpenAI(api_key="")  # Inserir a chave aqui

    response = client.chat.completions.create(
        messages= prompt,
        model= "gpt-3.5-turbo-0125",
        max_tokens= 4000,
        temperature= 0
    )
    return response.choices[0].message.content
