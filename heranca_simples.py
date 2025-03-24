class veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

    def ligar_motor(self):
        print("motor ligado")

class carro(veiculo):
    pass

class motocicleta(veiculo):
    pass

class caminhao(veiculo):
    pass

moto_vermelha = motocicleta("vermelho", "ABC-1234", 2)

moto_vermelha.ligar_motor()

fiat = carro("preto", "DEF-5678", 4)

fiat.ligar_motor()


man = caminhao("vermelho", "GHI-9012", 8)

man.ligar_motor()