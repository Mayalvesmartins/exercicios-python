class Midia:
    def __init__ (self, titulo, ano):
        self.titulo = titulo
        self.ano = ano


    def exibir_dados(self):
        print(f"titulo: {self.titulo}, ano: {self.ano}")

    
#herança
class Filme(Midia):
    def __init__(self, titulo, ano, diretor, duracao):
        super().__init__ (titulo, ano)
        self.diretor = diretor
        self.__duracao = duracao #encapsulamento

#polimorfismo
    def exibir_dados(self):
        print(f"titulo: {self.titulo}, ano: {self.ano}, diretor: {self.diretor} , duracao: {self.__duracao}")

#herança
class Livro(Midia):
    def __init__ (self, titulo, ano, autor, paginas):
        super().__init__(titulo, ano)
        self.autor = autor
        self.__paginas = paginas #encapsulamento

#polimorfismo
    def exibir_dados(self):
        print(f"titulo: {self.titulo}, ano: {self.ano} , autor: {self.autor}, paginas: {self.__paginas}")
    

mid = Midia ("o poço", 2022)
fil = Filme ("interestelar", 2000, "james", 2.35)
liv = Livro ("jogos vorazes", 2015, "suzane collins", 350)
mid.exibir_dados()
fil.exibir_dados()
liv.exibir_dados()
