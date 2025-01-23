class Veiculo:
    def mover(self):
        pass #Metodo abstrato

class Carro(Veiculo):
    def mover(self):
        print('O carro está se movendo.')

class Bicicleta(Veiculo):
    def mover(self):
        print("A bicicleta está se movendo.")
    

#Usando as  classes abstratas
carro = Carro()
carro.mover()

bicicleta = Bicicleta()
bicicleta.mover()