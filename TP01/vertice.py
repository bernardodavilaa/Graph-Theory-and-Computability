class Vertice:
    def __init__(self, id):
        self.id = id
        self.adjacentes = []

    def adicionar_adjacente(self, vertice):
        self.adjacentes.append(vertice)