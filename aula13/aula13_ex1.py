class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        return (f"Nome: {self.nome}, Salário: R${self.salario}")



class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_dados(self):
        return (f"Nome: {self.nome}, Salário: R${self.salario}, "
                f"Departamento: {self.departamento}")
        

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_dados(self):
        return (f"Nome: {self.nome}, Salário: R${self.salario}, "
                f"Linguagem: {self.linguagem}")


func = Funcionario("Ana", 3000)
ger = Gerente("Carlos", 8000, "TI")
dev = Desenvolvedor("Maria", 5000, "Python")
print(func.exibir_dados())
print(ger.exibir_dados())
print(dev.exibir_dados())