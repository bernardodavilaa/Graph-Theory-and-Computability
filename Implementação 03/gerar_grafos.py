import random
from collections import defaultdict

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def gerar_grafo_aleatorio(self, tamanho, arestas=None):
        max_edges = (tamanho * (tamanho - 1)) // 2

        if arestas is None:
            arestas = random.randint(tamanho - 1, tamanho * 10)

        arestas = min(arestas, max_edges)
        print(f"Gerando grafo aleatório com {tamanho} vértices e {arestas} arestas")

        existing_edges = set()
        
        # Adiciona arestas para garantir que o grafo esteja conectado
        for v in range(1, tamanho):
            self.adicionar_aresta(v, random.randint(0, v - 1))

        while len(existing_edges) < arestas:
            vertice1 = random.randint(0, tamanho - 1)
            vertice2 = random.randint(0, tamanho - 1)

            if vertice1 != vertice2:
                chave_aresta = (min(vertice1, vertice2), max(vertice1, vertice2))
                if chave_aresta not in existing_edges:
                    self.adicionar_aresta(vertice1, vertice2)
                    existing_edges.add(chave_aresta)

    def gerar_arvore_minima(self, tamanho):
        print(f"Gerando árvore geradora mínima com {tamanho} vértices e {tamanho - 1} arestas")

        for v in range(1, tamanho):
            self.adicionar_aresta(v, random.randint(0, v - 1))

    def salvar_em_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, 'w') as file:
            num_arestas = sum(len(arestas) for arestas in self.grafo.values()) // 2
            file.write(f"{self.V} {num_arestas}\n")
            for u in self.grafo:
                for v in self.grafo[u]:
                    if u < v:  # evita duplicação de arestas
                        file.write(f"{u} {v}\n")

# Função para gerar e salvar os grafos de diferentes tamanhos
def gerar_e_salvar_grafos():
    tamanhos = [10, 100, 1000, 10000]
    for tamanho in tamanhos:
        # Grafo Aleatório
        grafo_aleatorio = Grafo(tamanho)
        grafo_aleatorio.gerar_grafo_aleatorio(tamanho)
        grafo_aleatorio.salvar_em_arquivo(f"grafo_aleatorio_{tamanho}.txt")

        # Árvore Geradora Mínima
        agm = Grafo(tamanho)
        agm.gerar_arvore_minima(tamanho)
        agm.salvar_em_arquivo(f"agm_{tamanho}.txt")

if __name__ == "__main__":
    gerar_e_salvar_grafos()
