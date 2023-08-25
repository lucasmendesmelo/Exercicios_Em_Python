class Quadrado:
    
    def __init__(self, tamanhoLado):
        
        self.tamanhoLado = tamanhoLado
     
        
    def mudarValor(self, novoValor):
        
         self.tamanhoLado = novoValor   
        
        
    def retornaValor(self):
        
        return self.tamanhoLado
    
    
    def areaQuadrado(self):
        
        return self.tamanhoLado**2    