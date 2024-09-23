from ler_arquivo import ler_arquivo
from busca_profundidade import busca_profundidade, arestasArvore, arestasCruzamento, arestasAvanco

# Variáveis globais
global opcao

def main():
    global opcao
    global vetor_vertices_origem  # Declare a variável global aqui

    opcao = input("Digite '1' para ler '100.txt' ou '2' para ler '50000.txt': ")

    if opcao == '1':
        vertice_escolhido = int(input('Escolha um vértice de 1 a 100\n'))
        vetor_vertices_origem = ler_arquivo(opcao='1')
        
    else:
        vertice_escolhido = int(input('Escolha um vértice de 1 a 50.000\n'))
        vetor_vertices_origem = ler_arquivo(opcao='2')

    try:        
        busca_profundidade(vertice_escolhido, vetor_vertices_origem)
        
        print("Arestas da Árvore Encontradas:")
        for entrada, saida in arestasArvore:
            print(f"{entrada} -> {saida}")

        print(f"\nArestas que saem do Vértice {vertice_escolhido}:")

        for entrada, saida in arestasArvore:
            if entrada == vertice_escolhido:
                print(f"{entrada} -> {saida}"+ '   Aresta de Árvore')

        for entrada, saida in arestasCruzamento:
            if entrada == vertice_escolhido:
                print(f"{entrada} -> {saida}" '   Aresta de Cruzamento')

        for entrada, saida in arestasAvanco:
            if entrada == vertice_escolhido:
                print(f"{entrada} -> {saida}" '   Aresta de Avanço')

    except Exception as e:
        print("Ocorreu um erro inesperado:", str(e))

# Executa a função main
if __name__ == "__main__":
    main()
