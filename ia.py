import openai

# 🔑 coloque sua chave aqui
openai.api_key = "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"

def gerar_resposta(texto):
    print("🤖 Pensando...")

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente financeiro de banco, responda de forma clara e objetiva."
            },
            {"role": "user", "content": texto}
        ]
    )

    return resposta["choices"][0]["message"]["content"]