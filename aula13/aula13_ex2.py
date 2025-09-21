class Veiculo:
    def __init__(self, marca, velocidade):
        self.marca = marca
        self.velocidade = velocidade

    def mover (self):
        return (f"veiculo {self.marca} se movendo")

class Carro(Veiculo):
    def __init__(self, marca, velocidade, ligar_motor):
        super(). __init__ (marca, velocidade)
        self.ligar_motor = ligar_motor

    def exibir_dados (self):
        return (f"marca: {self.marca}, velocidade {self.velocidade}, modelo: {self.ligar_motor} ")
    
    def mover (self):
        return (f"Carro {self.marca} se movendo a velocidade {self.velocidade}")

class Bicicleta (Veiculo):
    def __init__(self, marca, velocidade, pedalar):
        super(). __init__(marca, velocidade)
        self.pedalar = pedalar


    def exibir_dados (self):
        return (f"marca {self.marca}, velocidade {self.velocidade}, pedalar {self.pedalar} ")


    def mover (self):
        return (f"Bicicleta {self.marca} se movendo a velocidade {self.velocidade}")
    

veiculos = [
    Carro("toyota", 120, "flex"), 
    Bicicleta("caloi", 25, "sim")  
]

for v in veiculos:
    print(v.mover())



        