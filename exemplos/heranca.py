class Animal:
    def __init__(self,nome):
        self.nome = nome

    def fazer_som(self):
        pass 
    
class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz au au")

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz miau!")

cachorro = Cachorro("Rex")
gato = Gato("Mimi")

cachorro.fazer_som()
gato.fazer_som()