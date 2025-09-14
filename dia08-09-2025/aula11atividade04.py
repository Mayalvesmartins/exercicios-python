class Livro:
    def __init__(self, titulo, autor, ano):
      
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_info(self):

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print("-" * 30)  



livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro3 = Livro("1984", "George Orwell", 1949)
livro4 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
livro5 = Livro("A Revolução dos Bichos", "George Orwell", 1945) 

livro1.exibir_info()
livro2.exibir_info()
livro3.exibir_info()
livro4.exibir_info()
livro5.exibir_info()