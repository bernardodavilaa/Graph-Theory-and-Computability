def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            primeira_linha = arquivo.readline().strip()
            num_ofertas, num_demandas = map(int, primeira_linha.split())

            lista_ofertas = [int(arquivo.readline().strip()) for _ in range(num_ofertas)]
            lista_demandas = [int(arquivo.readline().strip()) for _ in range(num_demandas)]

            matriz_custos = [
                list(map(int, arquivo.readline().strip().split())) 
                for _ in range(num_ofertas)
            ]

        return num_ofertas, num_demandas, lista_ofertas, lista_demandas, matriz_custos

    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        raise
