class ContaBancaria:
    def __init__ (self, saldo_inicial1=0):
        self.__saldo = saldo_inicial1

    def depositar (self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor invalido")

    def sacar (self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor invalido")

    def consultar_saldo (self):
        return self.__saldo
    
conta1 = ContaBancaria(0)
conta1.depositar(50)
conta1.sacar(30)
print("Saldo atual: ", conta1.consultar_saldo())
conta1.sacar(150)
print("Saldo atual: ", conta1.consultar_saldo())
conta1.depositar(20)
print("Saldo atual: ", conta1.consultar_saldo())
