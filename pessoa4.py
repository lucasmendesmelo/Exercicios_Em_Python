class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def imprimir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Peso:", self.peso)
        print("Altura:", self.altura)


# Programa principal
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))

pessoa = Pessoa(nome, idade, peso, altura)

pessoa.envelhecer()
pessoa.engordar(2.5)
pessoa.emagrecer(1.3)

pessoa.imprimir_informacoes()