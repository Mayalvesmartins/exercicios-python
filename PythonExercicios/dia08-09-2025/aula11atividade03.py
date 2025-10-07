produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade em estoque: "))


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas. Estoque atual: {self.quantidade}")

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades removidas. Estoque atual: {self.quantidade}")
        else:
            print("Erro: Quantidade solicitada maior do que o estoque disponível.")



produto1 = Produto(produto, preco, quantidade)

print(f"Produto: {produto1.nome}")
print(f"Preço unitário: R$ {produto1.preco}")
print(f"Quantidade em estoque: {produto1.quantidade}")
print(f"Valor total em estoque: R$ {produto1.calcular_valor_total()}")


produto1.adicionar_estoque(7)
produto1.remover_estoque(6)