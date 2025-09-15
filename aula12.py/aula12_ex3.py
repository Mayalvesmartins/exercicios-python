class Cliente:
    def __init__ (self, nome, email, cpf, saldo_inicial=0):
        self.nome = nome
        self.email = email
        self.__cpf = cpf
        self.__saldo = saldo_inicial

    def get_cpf(self):
        return self.__cpf
    
    def get_salario(self):
        return self.__saldo
    

    def adicionar_saldo (self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    def exibir_dados (self):
        return f"cliente: {self.nome} , email: {self.email}"
    
c1 = Cliente("Mayara", "mayalvesmartins@gmail.com", "123.456.789-00", 1000)
print(c1.exibir_dados())
print("CPF: ", c1.get_cpf())
print("Saldo: ", c1.get_salario())
if c1.adicionar_saldo(500):
    print("Novo saldo: ", c1.get_salario())

