class Retangulo:
    
    def __init__(self, ladoA, ladoB):
        
        self.ladoA = ladoA
        self.ladoB = ladoB
        
    def mudarValorLados(self, NovoLadoA, NovoLadoB):
        
        self.ladoA = NovoLadoA
        self.ladoB = NovoLadoB
        
    def retornaValorLados(self):
        
        print("LadoA: ", self.ladoA, "LadoB:", self.sladoB)    
            
    def calcularArea(self):
        
        return self.ladoA * self.ladoB
    
    def calcularPerimetro(self):
        
        return 2 * (self.ladoA + self.ladoB)
    
    
ladoA = float(input("Digite o valor do lado A do retângulo: "))
ladoB = float(input("Digite o valor do lado B do retângulo: "))

retangulo = Retangulo(ladoA, ladoB)

area = retangulo.calcularArea()
perimetro = retangulo.calcularPerimetro()

print("Área do retângulo:", area)
print("Perímetro do retângulo:", perimetro)