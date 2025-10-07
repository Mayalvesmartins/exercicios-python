class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


nota1 = input("Digite a nota: ")
nota2 = input("Digite a nota: ")

aluno1 = Aluno("Ana", float(nota1), float(nota2))
print(f"Nome: {aluno1.nome} , media: {aluno1.media()} , situacao: {aluno1.situacao()}")



nota3 = input("Digite a nota: ")
nota4 = input("Digite a nota: ")

aluno2 = Aluno("mayara" , float(nota3), float(nota4))
print(f"Nome: {aluno2.nome} , media: {aluno2.media()} , situacao: {aluno2.situacao()}")

