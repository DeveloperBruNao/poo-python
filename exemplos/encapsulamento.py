class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')
    
    def mostrar_saldo(self):
        print(f"Saldo: R$ {self.__saldo}")

conta = ContaBancaria("Bruno", 10000)
conta.depositar(500)
conta.sacar(100)
conta.mostrar_saldo()
