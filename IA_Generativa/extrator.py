import re

class Extrator:

    def extrair_valores(self, mensagem):
        mensagem = mensagem.lower()

        numeros = re.findall(r'\d+\.?\d*', mensagem)

        capital = None
        taxa = None
        tempo = None

        for n in numeros:
            valor = float(n)

            if "%" in mensagem and taxa is None:
                taxa = valor / 100

            elif "mes" in mensagem or "ano" in mensagem:
                tempo = int(valor)

            else:
                if capital is None:
                    capital = valor

    def extrair_dois_valores(self, mensagem):
        mensagem = mensagem.lower()
        numeros = re.findall(r'\d+\.?\d*', mensagem)
        if len(numeros) >= 2:
            return float(numeros[0]), float(numeros[1])
        return None, None