# Quadrado Class
class Quadrado:

    # Instance generator
    def __init__ (self, tamanho_lado=1):
        self.tamanho_lado = tamanho_lado
        
    # Returns the size of the square (one side)
    def retornarLado (self):
        return self.tamanho_lado
    
    # Changes the square side length
    def trocaLado (self, novo_tamanho_lado):
        self.tamanho_lado = novo_tamanho_lado
        print ("Tamanho do lado trocado para {}!".format(novo_tamanho_lado))

    # Computes the area of the square
    def calcularArea (self):
        print ("A área do quadrado é {}".format(self.tamanho_lado ** 2))

quadrado = Quadrado()
print ("O lado retornado é: {}".format(quadrado.retornarLado()))
quadrado.trocaLado(2)
quadrado.calcularArea()