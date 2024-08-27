#main.py
from ler_arquivo import ler_arquivo
from busca_profundidade import busca_profundidade

opcao = input("Digite '1' para ler '100.txt' ou '2' para ler '50000.txt': ")

#A primeira linha com a quantidade de vértices e arestas ficam nas variáveis, e o restante das linhas com as arestas estão nas variáveis arestas.

if opcao=='1':
    vertice_escolhido = input('Escolha um vértice de 1 a 100\n')
else:
    vertice_escolhido = input('Escolha um vértice de 1 a 50.000\n')


try:
    arestas = ler_arquivo(opcao) 
    let = busca_profundidade(arestas, vertice_escolhido)
    
except Exception as e:
    print("Ocorreu um erro inesperado", str(e))
    