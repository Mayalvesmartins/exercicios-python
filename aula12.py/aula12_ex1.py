class Funcionario:
    def __init__ (self, nome , salario):
        self.nome = nome
        self.__salario = salario

    def __str__ (self):
        return f"Nome: {self.nome}"

    
    def get_salario(self):
            return self.__salario         
    
    def set_salario(self, salario):
        self.__salario = salario 

funcionario1 = Funcionario("Joao" , 2000)
print(funcionario1)
print("Salario: ", funcionario1.get_salario())
funcionario1.set_salario(2500)
print("Novo salario: ", funcionario1.get_salario())



    
