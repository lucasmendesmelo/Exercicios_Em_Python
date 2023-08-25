class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if len(self.bucho) == 0:
            print("O bucho de", self.nome, "está vazio.")
        else:
            print("O bucho de", self.nome, "contém:")
            for alimento in self.bucho:
                print("-", alimento)

    def digerir(self):
        if len(self.bucho) == 0:
            print(self.nome, "não tem nada no bucho para digerir.")
        else:
            print(self.nome, "está digerindo...")
            self.bucho = []

# Programa principal
macaco1 = Macaco("Macaco 1")
macaco2 = Macaco("Macaco 2")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Laranja")

macaco2.comer("Pêssego")
macaco2.comer("Uva")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()

macaco1.comer(macaco2.nome)

macaco1.verBucho()
macaco2.verBucho()