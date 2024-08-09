#exibir_dados
def exibir_dados(grau_saida, grau_entrada, conjunto_sucessores, conjunto_predecessores):
    print('\n\n')
    linhas = [
        f"Grau de Saída: {grau_saida}",
        f"Grau de Entrada: {grau_entrada}",
        f"Conjunto de Sucessores: {conjunto_sucessores}",
        f"Conjunto de Predecessores: {conjunto_predecessores}"
    ]

    # Determinar o comprimento máximo da linha
    comprimento_max = max(len(linha) for linha in linhas)

    # Ajustar para aumentar a largura (adicionando espaços extras para margem)
    largura_extra = 20  # Aumentei a margem à direita
    comprimento_total = comprimento_max + largura_extra

    # Adicionar bordas e imprimir as linhas
    print("#" * (comprimento_total + 4))
    print(f"# {' ' * comprimento_total} #")  # Linha vazia no topo
    for linha in linhas:
        print(f"# {' ' * 4}{linha.ljust(comprimento_total - 4)} #")
    print(f"# {' ' * comprimento_total} #")  # Linha vazia na parte inferior
    print("#" * (comprimento_total + 4))

