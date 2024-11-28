#Método feito com IA

def exibir_resultados(matriz_alocacao, custo_total):
    print("\nResultado da Alocação:")

    largura_maxima = max(len(str(item)) for linha in matriz_alocacao for item in linha)
    linha_separacao = "   |   ".join('-' * largura_maxima for _ in range(len(matriz_alocacao[0])))

    for i, linha in enumerate(matriz_alocacao):
        linha_formatada = "   |   ".join(str(item).rjust(largura_maxima) for item in linha)
        print(f"| {linha_formatada} |") 
        if i < len(matriz_alocacao) - 1:
            print(f"| {linha_separacao} |")
    
    print(f"| {linha_separacao} |")

    print("\nCusto total do transporte:", custo_total)
    print()  # Adiciona um espaço extra após o custo total
