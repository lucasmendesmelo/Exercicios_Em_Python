class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def alterarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo alcançado.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo alcançado.")

    def informacoesTV(self):
        print("Canal:", self.canal)
        print("Volume:", self.volume)


# Programa principal
tv = TV()

while True:
    print("\n------ Controle da TV ------")
    print("1. Alterar canal")
    print("2. Aumentar volume")
    print("3. Diminuir volume")
    print("4. Desligar TV")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        novo_canal = int(input("Digite o número do novo canal: "))
        tv.alterarCanal(novo_canal)
    elif opcao == 2:
        tv.aumentarVolume()
    elif opcao == 3:
        tv.diminuirVolume()
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Tente novamente.")

    tv.informacoesTV()