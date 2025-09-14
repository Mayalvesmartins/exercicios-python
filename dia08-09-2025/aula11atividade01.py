class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f"Marca: {self.marca} , modelo: {self.modelo} , Ano: {self.ano}")
       

meu_carro1 = Carro("Toyota", "Corolla", 2020)
meu_carro2 = Carro("porche", "porche", 2025)
meu_carro3 = Carro("chevrolet", "onix" , 2021)

meu_carro1.exibir_dados()
meu_carro2.exibir_dados()
meu_carro3.exibir_dados()