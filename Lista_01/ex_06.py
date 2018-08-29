# TV class
class TV:

    # Instance generator
    def __init__ (self, canal = 1, volume_inicial = 20):
        if (canal < 0) or (canal > 255):
            print ("O canal escolhido é inválido, colocando canal padrão = 1")
            self.canal = 1
        else:
            self.canal = canal
        if (volume_inicial < 0) or (volume_inicial > 100):
            print ("O volume inicial escolhido é inválido, colocando o volume inicial padrão = 20")
            self.volume = 20
        else:
            self.volume = volume_inicial
    
    # Chooses TV channel
    def mudarCanal (self, canal):
        if (canal < 0) or (canal > 255):
            print ("Canal escolhido inválido")
        else:
            self.canal = canal

    # Increases sound volume
    def aumentarVolume (self):
        if (self.volume < 100):
            self.volume += 1
    
    # Decreases sound volume
    def diminuirVolume (self):
        if (self.volume > 0):
            self.volume -= 1