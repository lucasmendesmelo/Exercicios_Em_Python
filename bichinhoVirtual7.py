class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, novo_valor):
        self.fome = novo_valor

    def alterarSaude(self, novo_valor):
        self.saude = novo_valor

    def alterarIdade(self, novo_valor):
        self.idade = novo_valor

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        humor = (self.fome + self.saude) / 2
        return humor


# Programa principal
bichinho = BichinhoVirtual("Tamagushi")

bichinho.alterarFome(80)
bichinho.alterarSaude(60)
bichinho.alterarIdade(2)

print("Nome:", bichinho.retornarNome())
print("Fome:", bichinho.retornarFome())
print("Saúde:", bichinho.retornarSaude())
print("Idade:", bichinho.retornarIdade())
print("Humor:", bichinho.retornarHumor())