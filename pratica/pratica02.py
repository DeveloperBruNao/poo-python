class Carro:
    def __init__(self,ano,cor,motor,placa,modelo):
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.placa = placa
        self.modelo = modelo
    
    def Ano(self):
        return f'O ano do carro é: {self.ano}'
    
    def Cor(self):
        return f'A cor do carro é: {self.cor} '
    
    def Motor(self):
        return f'O motor do carro é: {self.motor}'
    
    def Placa(self):
        return f'A placa do carro é: {self.placa}'
    
    def Modelo(self):
        return f'A placa do carro é: {self.modelo}'

carro = Carro('2007','Preto','v8','KFC-597','Lancer EVO')

# Chamando os métodos individualmente
print(carro.Ano())
print(carro.Cor())
print(carro.Motor())
print(carro.Placa())
print(carro.Modelo())