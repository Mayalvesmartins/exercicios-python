class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def __str__ (self):
        return f"Produto: {self.__nome}, Preco: {self.__preco}, Estoque: {self.__estoque}"
    
    
    def get_nome (self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_estoque(self):
        return self.__estoque
    
    def aplicar_desconto(self, percentual):
        if 0 < percentual < 100:
            desconto = self.__preco * (percentual / 100)
            self.__preco -= desconto
            return True
        return False
    

produto1 = Produto ("notebook", 3000, 10)
print(produto1)
if produto1.aplicar_desconto(10):
    print("Novo preco com desconto: ", produto1.get_preco())