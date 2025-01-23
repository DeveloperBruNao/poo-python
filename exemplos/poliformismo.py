class Formato:
    def desenhar(self):
        pass

class Circulo(Formato):
    def desenhar(self):
        print(f"Desenhando um círculo")

class Quadrado(Formato):
    def desenhar(self):
        print("Desenhando um quadrado.")

formas = [Circulo(), Quadrado()]

for forma in formas:
    forma.desenhar()