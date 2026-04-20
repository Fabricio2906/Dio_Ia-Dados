from openai import OpenAI
import os

class IA:
    def __init__(self):
        self.client = OpenAI(api_key="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")
        self.historico = [
            {"role": "system", "content": "Você é um assistente financeiro claro, objetivo e didático."}
        ]
    def perguntar(self, mensagem):
        self.historico.append({"role": "user", "content": mensagem})

        try:
            resposta = self.client.chat.completions.create(
                model = "gpt-4o-mini",
                messages = self.historico 
            )
            resposta_texto = resposta.choices[0].message.content

            self.historico.append({"role": "assistant", "content": resposta_texto})
            return resposta_texto
        except RateLimitError:
            return "Desculpe, atingi o limite de uso da API. Verifique sua conta OpenAI."
        except Exception as e:
            return f"Erro ao processar a pergunta: {str(e)}"