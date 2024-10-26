from collections import defaultdict, deque

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(lambda: defaultdict(int))  # Grafo com capacidades

    def adiciona_aresta(self, u, v, capacidade=1):
        self.grafo[u][v] = capacidade

    def bfs(self, origem, destino, pai):
        # Realiza uma busca em largura para encontrar um caminho aumentante
        visitado = [False] * self.V
        fila = deque([origem])
        visitado[origem] = True

        while fila:
            u = fila.popleft()
            for v, capacidade in self.grafo[u].items():
                if not visitado[v] and capacidade > 0:
                    fila.append(v)
                    visitado[v] = True
                    pai[v] = u
                    if v == destino:
                        return True
        return False

    def fluxo_maximo(self, origem, destino):
        pai = [-1] * self.V
        fluxo_maximo = 0

        # Aumenta o fluxo enquanto há caminhos aumentantes
        while self.bfs(origem, destino, pai):
            caminho_fluxo = float('Inf')
            v = destino
            while v != origem:
                u = pai[v]
                caminho_fluxo = min(caminho_fluxo, self.grafo[u][v])
                v = pai[v]

            # Atualiza as capacidades residuais das arestas e arestas reversas
            v = destino
            while v != origem:
                u = pai[v]
                self.grafo[u][v] -= caminho_fluxo
                self.grafo[v][u] += caminho_fluxo
                v = pai[v]

            fluxo_maximo += caminho_fluxo

        return fluxo_maximo

## Método do TP01
def ler_grafo_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as file:
            linhas = file.readlines()

        if len(linhas) < 2:
            raise ValueError(f"O arquivo {caminho_arquivo} não possui linhas suficientes para definir o grafo.")

        num_vertices, num_arestas = map(int, linhas[0].split())
        grafo = Grafo(num_vertices)

        for i in range(1, num_arestas):
            if i >= len(linhas):
                raise ValueError(f"O arquivo {caminho_arquivo} não possui linhas suficientes para todas as arestas declaradas.")
            u, v = map(int, linhas[i].split())
            grafo.adiciona_aresta(u, v)

        if num_arestas + 1 >= len(linhas):
            raise ValueError(f"O arquivo {caminho_arquivo} não possui uma linha para a origem e destino.")
        
        origem, destino = map(int, linhas[num_arestas + 1].split())
        return grafo, origem, destino
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    except ValueError as ve:
        print(f"Erro no formato do arquivo {caminho_arquivo}: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo {caminho_arquivo}: {e}")
    return None, None, None

