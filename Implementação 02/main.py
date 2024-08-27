from ler_arquivo import ler_arquivo
from busca_profundidade import busca_profundidade

opcao = input("Digite '1' para ler '100.txt' ou '2' para ler '50000.txt': ")
global num_vertices, tempoDescoberta, tempoTermino, arestasArvore, arestasRetorno, vetor_vertices_origem

if opcao == '1':
    vertice_escolhido = int(input('Escolha um vértice de 1 a 100\n'))
    num_vertices = 100
else:
    vertice_escolhido = int(input('Escolha um vértice de 1 a 50.000\n'))
    num_vertices = 50000

try:
    tempoDescoberta = [None] * (num_vertices)
    tempoTermino = [None] * (num_vertices)
    arestasArvore = arestasRetorno =[]
    
    vetor_vertices_origem = ler_arquivo(opcao) 
    let = busca_profundidade(vertice_escolhido)
    
except Exception as e:
    print("Ocorreu um erro inesperado", str(e))
