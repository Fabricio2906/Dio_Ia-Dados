class Contexto:

    def __init__(self):
        self.historico = []

        def adicionar(self, role, mensagem):
            self.historico.append({
            "role": role,
            "content": mensagem
        })

        def obter_historico(self):
            return self.historico