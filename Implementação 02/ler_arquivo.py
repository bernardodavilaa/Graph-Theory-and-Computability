def ler_arquivo(opcao):
    # Dicionário para mapear as opções do usuário para os nomes dos arquivos
    opcoes_arquivo = {
        '1': 'grafos-100.txt',
        '2': 'grafos-50000.txt'
    }

    # Determinando o nome do arquivo com base na escolha do usuário
    nome_arquivo = opcoes_arquivo.get(opcao)

    if nome_arquivo:
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                if not linhas:
                    return []

                # Processar a primeira linha para obter num_vertices e num_arestas
                primeira_linha = linhas[0].split()
                try:
                    num_vertices = int(primeira_linha[0])
                    num_arestas = int(primeira_linha[1])
                except (ValueError, IndexError):
                    print("Formato inválido na primeira linha do arquivo.")
                    return []

                # Processar as linhas restantes para obter as arestas
                arestas = []
                for linha in linhas[1:]:
                    partes = linha.split()
                    if len(partes) == 2:
                        try:
                            vertice_entrada = int(partes[0])
                            vertice_saida = int(partes[1])
                            aresta = {"vertice_entrada": vertice_entrada, "vertice_saida": vertice_saida}
                            arestas.append(aresta)
                        except ValueError:
                            continue

                return arestas

        except Exception as e:
            print("Erro ao ler o arquivo:", str(e))
            return []
    else:
        print("Opção inválida.")
        return []
