# Pessoa Class
class Pessoa:

    # Instance generator
    def __init__ (self, nome = "", idade = 0, peso = 0.0, altura = 0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    # Gets older
    def envelhecer (self):
        if (self.idade < 21):
            self.crescer()
        self.idade += 1
        print ("Você envelheceu o(a) {}".format(self.nome))

    # Gains weight
    def engordar (self):
        self.peso += 1
        print ("Você engordou o(a) {}".format(self.nome))

    # Loses weight
    def emagrecer (self):
        self.peso -= 1
        print ("Você emagreceu o(a) {}".format(self.nome))
    
    # Gets taller
    def crescer (self):
        self.altura += 0.05

pessoa = Pessoa("Gabriel", 15, 70, 1.8)
pessoa.envelhecer()
print (pessoa.altura)