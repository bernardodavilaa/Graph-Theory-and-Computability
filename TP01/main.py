from grafo import Grafo

def main():
    print("Escolha um tamanho de grafo:")
    print("1. 10 vértices")
    print("2. 100 vértices")
    print("3. 1000 vértices")
    print("4. 100000 vértices")
    
    escolha_tamanho = input("Digite o número de vértices do grafo: ")

    # Mapeia a escolha para o número de vértices
    if escolha_tamanho == "1":
        tamanho = 10
    elif escolha_tamanho == "2":
        tamanho = 100
    elif escolha_tamanho == "3":
        tamanho = 1000
    elif escolha_tamanho == "4":
        tamanho = 100000
    else:
        print("Escolha inválida.")
        return

    print("Escolha o tipo de grafo:")
    print("1. Gerar grafo aleatório")
    print("2. Gerar árvore geradora mínima")
    
    escolha_tipo = input("Digite o número do tipo de grafo: ")

    g = Grafo(tamanho)

    if escolha_tipo == "1":
        g.gerar_grafo_aleatorio(tamanho)
    elif escolha_tipo == "2":
        g.gerar_arvore_minima(tamanho)  # Chama o método para gerar árvore geradora mínima
    else:
        print("Escolha inválida.")
        return

    if g.verificar_ciclos():
        print("O grafo contém ciclos.")
    else:
        print("O grafo não contém ciclos.")
    
    articulacoes = g.encontrar_vertices_articulacao()  # Captura as articulações
    if articulacoes:
        print(f"Articulações encontradas: {articulacoes}")
    else:
        print("Não foram encontradas articulações.")

    componentes = g.algoritmo_tarjan()
    print("Componentes Fortemente Conectados:", componentes)

if __name__ == "__main__":
    main()
