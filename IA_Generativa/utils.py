class Utils:

    def identifier(self, mensagem):
        mensagem = mensagem.lower()

        if "soma" in mensagem:
            return "soma"
        if "subtração" in mensagem or "subtracao" in mensagem:
            return "subtracao"
        if "multiplicação" in mensagem or "multiplicacao" in mensagem:
            return "multiplicacao"
        if "divisão" in mensagem or "divisao" in mensagem:
            return "divisao"

        if "juros" in mensagem:
            return "juros"
        
        if "parcela" in mensagem:
            return "parcela"
        
        return "calculo"