class Carro:
    def __init__(self,marca,modelo,cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def ligar(self):
        print(f'O {self.marca} {self.modelo} está ligado.')

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota","Corolla", "Prata")

# Acessando atributos do objeto
print(meu_carro.marca)
meu_carro.ligar()
