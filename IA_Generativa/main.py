from ia import IA
from calculos import Calculos
from utils import Utils
from extrator import Extrator

ia = IA()
calc = Calculos()
utils = Utils()
extrator = Extrator()

print("💬 IA Financeira iniciada!\n")

while True:
    mensagem = input("Você: ")

    if mensagem.lower() == "sair":
        break

    tipo = utils.identifier(mensagem)

    if tipo == "juros":
        capital, taxa, tempo = extrator.extrair_valores(mensagem)
        if capital and taxa and tempo:
            valores = [capital, taxa, tempo]
            resultado = calc.executar_operacao(tipo, valores)
            print(f"IA: O valor final será R${resultado:.2f}")
        else:
            print("IA: Não consegui entender os valores. Tente algo como: 1000 reais a 5% por 12 meses")

    else:
        resposta = ia.perguntar(mensagem)
        print("IA:", resposta)