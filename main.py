#main.py
from exibir_dados import exibir_dados
from ler_arquivo import ler_arquivo
from busca_grafo import forward_star

opcao = input("Digite '1' para ler 'grafos-100.txt' ou '2' para ler 'grafos-50000.txt': ")

quantidade_vertices, quantidade_arestas, arestas = ler_arquivo(opcao)
arcOrig = []
arcDest = []
pointer = []
pointer.append(0)

if opcao=='1':
    vertice_escolhido = input('Escolha um vértice de 1 a 100\n')
else:
    vertice_escolhido = input('Escolha um vértice de 1 a 50.000\n')

num1_anterior = None

try:
    for contador, (num1, num2) in enumerate(arestas, start=0):
        arcOrig.append(num1)
        arcDest.append(num2)
        
        if num1 != num1_anterior and num1_anterior is not None:
            pointer.append(contador)
            
        num1_anterior = num1
        
    grau_saida, grau_entrada, conjunto_sucessores, conjunto_predecessores = forward_star(arcOrig, arcDest, pointer, int(vertice_escolhido)) 
    
    exibir_dados(grau_saida, grau_entrada, conjunto_sucessores, conjunto_predecessores) 

except Exception as e:
    print("Ocorreu um erro inesperado", str(e))
    