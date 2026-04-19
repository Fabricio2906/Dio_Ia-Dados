from talk import gravar_audio, transcrever_audio
from ia import gerar_resposta
from tts import falar

def interpretar_comando(texto):
    texto = texto.lower()

    if "gasto total" in texto:
        gastos = [100, 250, 80]
        return f"Seu gasto total foi de {sum(gastos)} reais"

    if "saldo" in texto:
        return "Seu saldo atual é de 1250 reais"

    return None

def main():
    arquivo = gravar_audio()
    texto = transcrever_audio(arquivo)

    resposta_local = interpretar_comando(texto)

    if resposta_local:
        resposta = resposta_local
    else:
        resposta = gerar_resposta(texto)

    print(f"💬 Resposta: {resposta}")
    falar(resposta)

if __name__ == "__main__":
    main()