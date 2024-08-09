# arquivo_funcoes.py

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
                    return None, None, None

                # Processar a primeira linha para obter num_vertices e num_arestas
                primeira_linha = linhas[0].split()
                try:
                    num_vertices = int(primeira_linha[0])
                    num_arestas = int(primeira_linha[1])
                except (ValueError, IndexError):
                    print("Formato inválido na primeira linha do arquivo.")
                    return None, None, None

                # Processar as linhas restantes para obter pares de números
                pares_numeros = []
                for linha in linhas[1:]:
                    partes = linha.split()
                    if len(partes) == 2:
                        try:
                            num1 = int(partes[0])
                            num2 = int(partes[1])
                            pares_numeros.append((num1, num2))
                        except ValueError:
                            continue

                return num_vertices, num_arestas, pares_numeros

        except Exception as e:
            print("Erro ao ler o arquivo:", str(e))
            return None, None, None
    else:
        print("Opção inválida.")
        return None, None, None
