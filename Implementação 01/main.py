#main.py
from exibir_dados import exibir_dados
from ler_arquivo import ler_arquivo
from busca_grafo import forward_star

opcao = input("Digite '1' para ler 'grafos-100.txt' ou '2' para ler 'grafos-50000.txt': ")

#A primeira linha com a quantidade de vértices e arestas ficam nas variáveis, e o restante das linhas com as arestas estão nas variáveis arestas.
quantidade_vertices, quantidade_arestas, arestas = ler_arquivo(opcao)
arcOrig = []
arcDest = []
pointer = []
pointer.append(0)

if opcao=='1':
    vertice_escolhido = input('Escolha um vértice de 1 a 100\n')
else:
    vertice_escolhido = input('Escolha um vértice de 1 a 50.000\n')

vertice_origem_anterior = None

try:
    # arcOrig = vetor com vértices de origem || arcDest = vetor com vértices de destino || pointer = vetor com as posições dos vértices nos vetores arcOrig e arcDest
    for contador, (vertice_origem, vertice_destino) in enumerate(arestas, start=0):
        arcOrig.append(vertice_origem)
        arcDest.append(vertice_destino)
        
        if vertice_origem != vertice_origem_anterior and vertice_origem_anterior is not None:
            pointer.append(contador)
            
        vertice_origem_anterior = vertice_origem
    
    # Método utilizado para busca no grafo forwardstar
    grau_saida, grau_entrada, conjunto_sucessores, conjunto_predecessores = forward_star(arcOrig, arcDest, pointer, int(vertice_escolhido)) 
    
    exibir_dados(grau_saida, grau_entrada, conjunto_sucessores, conjunto_predecessores) 

except Exception as e:
    print("Ocorreu um erro inesperado", str(e))
    