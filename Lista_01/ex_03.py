# Retangulo Class
class Retangulo:

    # Instance generator
    def __init__ (self, base=1, altura=1):
        self.base = base
        self.altura = altura
        
    # Returns the sizes of the rectangle (both sides)
    def retornarLado (self):
        return self.base, self.altura
    
    # Changes the rectangle sides length
    def trocaLados (self, nova_base=0, nova_altura=0):
        if (nova_altura != 0):
            self.altura = nova_altura

        if (nova_base != 0):
            self.base = nova_base

        print ("Os novos lados do retângulo são {} e {}".format(self.base, self.altura))

    # Computes the area of the rectangle
    def calcularArea (self):
        return(self.base * self.altura)

    # Computes the perimeter of the rectangle
    def calcularPerimetro (self):
        return(2 * self.base + 2 * self.altura)

###
# Testing
###
lado1 = float(input("Qual a medida de um lado da sala? >>> "))
lado2 = float(input("Qual a medida do outro lado da sala? >>> "))

retangulo = Retangulo(lado1, lado2)

area = retangulo.calcularArea()
perimetro = retangulo.calcularPerimetro()

print ("Você precisará de {}m² de piso na sala e de {}m de rodapé!".format(area, perimetro))