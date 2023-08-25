class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            print("Foram abastecidos {:.2f} litros de {}.".format(litros_abastecidos, self.tipoCombustivel))
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecerPorLitro(self, litros):
        valor_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print("O valor a ser pago é R${:.2f}.".format(valor_pagar))
        else:
            print("Não há combustível suficiente na bomba.")

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade


# Programa principal
bomba = BombaCombustivel("Gasolina", 4.5, 1000)

print("Tipo de combustível:", bomba.tipoCombustivel)
print("Valor do litro:", bomba.valorLitro)
print("Quantidade de combustível:", bomba.quantidadeCombustivel)

bomba.abastecerPorValor(50)
bomba.abastecerPorLitro(20)

bomba.alterarValor(4.8)
bomba.alterarCombustivel("Etanol")
bomba.alterarQuantidadeCombustivel(800)

print("Tipo de combustível:", bomba.tipoCombustivel)
print("Valor do litro:", bomba.valorLitro)
print("Quantidade de combustível:", bomba.quantidadeCombustivel)