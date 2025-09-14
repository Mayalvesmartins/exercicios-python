class Aluno:
    def __init__(self):
        self.nome = input("Digite o nome: ")
        self.nota1 = float(input("Digite a primeira nota: "))
        self.nota2 = float(input("Digite a segunda nota: "))

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
    
    def printar(self):
        print(f"Sua nota foi {self.media()}, e voce esta {self.situacao()}")
    
aluno1 = Aluno()

aluno1.printar()







