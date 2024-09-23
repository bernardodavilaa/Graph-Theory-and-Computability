class vertice:
    # Atributos
    def __init__(self):
        self.successors = []  # Lista de sucessores
        self.td = None        # Tempo de descoberta
        self.tt = None        # Tempo de término
        self.parent = None     # Vértice pai

    # Getters
    def get_successors(self):
        return self.successors

    def get_td(self):
        return self.td

    def get_tt(self):
        return self.tt

    def get_parent(self):
        return self.parent

    # Setters
    def set_td(self, td):
        self.td = td

    def set_tt(self, tt):
        self.tt = tt

    def set_parent(self, parent):
        self.parent = parent

    # Métodos
    def add_successor(self, value):
        self.successors.append(value)


