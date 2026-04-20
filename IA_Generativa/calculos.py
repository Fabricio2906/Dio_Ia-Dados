class Calculos:

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Divisão por zero não é permitida.")

    def juros_simples(self, capital, taxa, tempo):
        return capital * taxa * tempo

    def juros_compostos(self, capital, taxa, tempo):
        return capital * (1 + taxa) ** tempo

    def calcular_parcela(self, valor, parcelas):
        return valor / parcelas