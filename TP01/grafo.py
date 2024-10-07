import random
from vertice import Vertice

class Grafo:
    def __init__(self, tamanho):
        self.vertices = [Vertice(i) for i in range(tamanho)]
        self.indice = 0
        self.pilha = []
        self.visitado = [-1] * tamanho  # -1 indica que o vértice ainda não foi visitado
        self.nao_processado = [-1] * tamanho  # -1 indica que o vértice ainda não foi processado
        self.componentes_fortemente_conexos = []
        
    ## Geração de grafo (Aleatório, árvore ou Manual)

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre dois vértices
        self.vertices[u].adicionar_adjacente(v)
        self.vertices[v].adicionar_adjacente(u)

    def gerar_grafo_aleatorio(self, tamanho, arestas=None):
        max_edges = (tamanho * (tamanho - 1)) // 2

        if arestas is None:
            arestas = random.randint(tamanho - 1, tamanho * 10)

        arestas = min(arestas, max_edges)
        print(f"Gerando grafo com {tamanho} vértices e {arestas} arestas")

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

    def verificar_ciclos(self):
    # Verifica se há ciclos no grafo usando DFS
        visitados = set()

        for vertice in self.vertices:
            if vertice.id not in visitados:
                pilha = [(vertice, None)]  # A pilha contém pares (nó, nó pai)

                while pilha:
                    (vertice_atual, pai) = pilha.pop()
                    if vertice_atual.id in visitados:
                        continue

                    visitados.add(vertice_atual.id)
                    for adj in vertice_atual.adjacentes:
                        if self.vertices[adj].id not in visitados:
                            pilha.append((self.vertices[adj], vertice_atual.id))
                        elif pai != self.vertices[adj].id:
                            return True
        return False

    def encontrar_vertices_articulacao(self):
        visitados = [False] * len(self.vertices)
        descoberta = [0] * len(self.vertices)
        baixo = [0] * len(self.vertices)
        pai = [-1] * len(self.vertices)
        vertices_articulacao = set()
        tempo = [0]

        for i in range(len(self.vertices)):
            if not visitados[i]:
                pilha = [(i, None)]
                while pilha:
                    (vertice, parent) = pilha.pop()
                    if visitados[vertice]:
                        continue
                    visitados[vertice] = True
                    descoberta[vertice] = baixo[vertice] = tempo[0]
                    tempo[0] += 1
                    filhos = 0
                    for vizinho in self.vertices[vertice].adjacentes:
                        if not visitados[vizinho]:
                            pai[vizinho] = vertice
                            filhos += 1
                            pilha.append((vizinho, vertice))
                            baixo[vertice] = min(baixo[vertice], baixo[vizinho])
                            if pai[vertice] == -1 and filhos > 1:
                                vertices_articulacao.add(vertice)
                            if pai[vertice] != -1 and baixo[vizinho] >= descoberta[vertice]:
                                vertices_articulacao.add(vertice)
                        elif vizinho != pai[vertice]:
                            baixo[vertice] = min(baixo[vertice], descoberta[vizinho])
        return vertices_articulacao
    ## Algoritmo de Tarjan

    def algoritmo_tarjan(self):
        # Executa o algoritmo de Tarjan para encontrar componentes fortemente conectados
        for vertice in range(len(self.vertices)):
            if self.visitado[vertice] == -1:
                pilha = [vertice]
                while pilha:
                    v = pilha[-1]
                    if self.visitado[v] == -1:
                        self.visitado[v] = self.indice
                        self.nao_processado[v] = self.indice
                        self.indice += 1
                        self.pilha.append(v)
                        for vizinho in self.vertices[v].adjacentes:
                            if self.visitado[vizinho] == -1:
                                pilha.append(vizinho)
                            elif vizinho in self.pilha:
                                self.nao_processado[v] = min(self.nao_processado[v], self.visitado[vizinho])
                    else:
                        pilha.pop()
                        if self.nao_processado[v] == self.visitado[v]:
                            componente = []
                            while True:
                                w = self.pilha.pop()
                                componente.append(w)
                                if w == v:
                                    break
                            self.componentes_fortemente_conexos.append(componente)
                        if pilha:
                            self.nao_processado[pilha[-1]] = min(self.nao_processado[pilha[-1]], self.nao_processado[v])
        return self.componentes_fortemente_conexos
