# Bola Class
class Bola:

    # Instance generator
    def __init__ (self, cor = "", circunferencia = "", material = ""):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    # Shows the ball color
    def mostraCor (self):
        print ("A cor da bola é: {}".format(self.cor))
    
    # Changes the ball color
    def trocaCor (self, nova_cor):
        self.cor = nova_cor
        print ("Cor trocada para {}!".format(nova_cor))

bola = Bola()
bola.mostraCor()
bola.trocaCor("Vermelho")
bola.mostraCor()