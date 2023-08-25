class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para realizar o saque.")

    def imprimirInformacoes(self):
        print("Número da conta:", self.numero_conta)
        print("Nome do correntista:", self.nome_correntista)
        print("Saldo:", self.saldo)


# Programa principal
numero_conta = input("Digite o número da conta corrente: ")
nome_correntista = input("Digite o nome do correntista: ")

conta = ContaCorrente(numero_conta, nome_correntista)

conta.deposito(1000)
conta.saque(500)

conta.imprimirInformacoes()