class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("Coordenadas do ponto: ({}, {})".format(self.x, self.y))


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)


# Função para exibir um menu de opções
def exibirMenu():
    print("\n------ Menu ------")
    print("1. Alterar retângulo")
    print("2. Imprimir centro do retângulo")
    print("3. Sair")


# Programa principal
ponto_inicial = Ponto(0, 0)
retangulo = Retangulo(ponto_inicial, 5, 3)

while True:
    exibirMenu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        x = int(input("Digite o valor de x do ponto inicial: "))
        y = int(input("Digite o valor de y do ponto inicial: "))
        largura = int(input("Digite a largura do retângulo: "))
        altura = int(input("Digite a altura do retângulo: "))

        ponto_inicial = Ponto(x, y)
        retangulo = Retangulo(ponto_inicial, largura, altura)
    elif opcao == 2:
        centro = retangulo.encontrarCentro()
        centro.imprimir()
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")