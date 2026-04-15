#Venda de gutin

class Gutin:
    def __init__(self, sabor, localidade, marca, vendedor, id_gutin = None):
        self.id_gutin = id_gutin
        self.sabor = sabor
        self.localidade = localidade
        self.marca = marca
        self.vendedor = vendedor


    def __str__(self):
        return f"ID: {self.id_gutin}, Sabor: {self.sabor}, Localidade: {self.localidade}, Marca: {self.marca}, Vendedor: {self.vendedor}."    
