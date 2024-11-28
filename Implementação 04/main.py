from ler_arquivo import ler_arquivo
from exibir_resultados import exibir_resultados
from obter_arquivo import obter_arquivo_escolhido
#from gerar_pdf import gerar_pdf

def dual():
    arquivo_base = obter_arquivo_escolhido()

    if not arquivo_base:
        print("Opção inválida. Tente novamente.")
        return

    caminho_arquivo = f"Implementação 04/{arquivo_base}"

    try:
        num_ofertas, num_demandas, lista_ofertas, lista_demandas, matriz_custos = ler_arquivo(caminho_arquivo)
        matriz_alocacao = [[0] * num_demandas for _ in range(num_ofertas)]
        custo = 0

        # Alocação
        for x in range(num_ofertas):
            for y in range(num_demandas):
                if lista_ofertas[x] > 0 and lista_demandas[y] > 0:
                    quantidade_alocada = min(lista_ofertas[x], lista_demandas[y])
                    matriz_alocacao[x][y] = quantidade_alocada
                    lista_ofertas[x] -= quantidade_alocada
                    lista_demandas[y] -= quantidade_alocada
                    custo += quantidade_alocada * matriz_custos[x][y]

        exibir_resultados(matriz_alocacao, custo)

        # Gerar PDF com os resultados
        #gerar_pdf(arquivo_base, matriz_alocacao, custo)

    except Exception as erro:
        print(f"Ocorreu um problema: {erro}")


if __name__ == "__main__":
    dual()
