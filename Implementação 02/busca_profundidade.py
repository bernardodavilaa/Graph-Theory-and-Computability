from ler_arquivo import ler_arquivo
from vertice import vertice

num_vertices = 50000
vertice = [vertice() for _ in range(num_vertices)]
arestasArvore = []
arestasRetorno = []
arestasAvanco = []
arestasCruzamento = []
tempo = 0

visitados = set()

def busca_profundidade(v, vetor_vertices_origem):
    global tempo
    if v in visitados:
        return 

    tempo += 1
    vertice[v].set_td(tempo)
    
    visitados.add(v)

    for aresta in vetor_vertices_origem[v]:
        if aresta['vertice_entrada'] == v:
            if vertice[aresta['vertice_saida']].get_td() is None:
                arestasArvore.append((v, aresta['vertice_saida']))
                vertice[aresta['vertice_saida']].set_parent(aresta['vertice_entrada'])
                busca_profundidade(aresta['vertice_saida'], vetor_vertices_origem)
            else:
                if vertice[aresta['vertice_saida']].get_tt() is None:
                    arestasRetorno.append((v, aresta['vertice_saida']))
                elif vertice[aresta['vertice_entrada']].get_td() is None < vertice[aresta['vertice_saida']].get_tt():
                    arestasAvanco.append((v, aresta['vertice_saida']))
                else:
                    arestasCruzamento.append((v, aresta['vertice_saida']))

    tempo += 1
    vertice[v].set_tt(tempo)

    return vertice[v].get_td()

def obter_arestas():
    return {
        "arestas_arvore": arestasArvore,
        "arestas_retorno": arestasRetorno,
        "arestas_avanco": arestasAvanco,
        "arestas_cruzamento": arestasCruzamento
    }
