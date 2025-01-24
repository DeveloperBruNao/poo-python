class Calculadora:
    def soma(self, numero1, numero2):
        return numero1 + numero2
    
    def subtracao(self, numero1, numero2):
        return numero1 - numero2
    
    def multiplicacao(self, numero1, numero2):
        return numero1 * numero2
    
    def divisao(self, numero1, numero2):
        if numero1 or numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero não é permitida"
    
calc = Calculadora()
print('Bem vindo a calculadora')
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Operações
print(f"Soma: {calc.soma(numero1, numero2)}")
print(f"Subtração: {calc.subtracao(numero1, numero2)}")
print(f"Multiplicação: {calc.multiplicacao(numero1, numero2)}")
print(f"Divisão: {calc.divisao(numero1, numero2)}")