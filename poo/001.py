class Televisao:
    def __init__(self, marca, tamanho, canal, volume, ligada=False, volume_max=30, canal_max=800):
        self.marca=marca
        self.tamanho=tamanho
        self.canal=canal
        self.volume=volume
        self.volume_max = volume_max
        self.canal_max = canal_max
        self.ligada = ligada

    def ligarDesligar(self):
        self.ligada = True
        print("Essa bosta ligou")

    def trocarCanal(numero):
        def trocarVolume():
            print("trocou de canal")

    def mostrar():
        print("mostrou")



tv = Televisao ("samnugn", "50px", "canal do boi", "300")

print(tv.tamanho)
print(tv.ligarDesligar())
    
