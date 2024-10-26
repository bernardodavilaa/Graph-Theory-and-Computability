import time
from Grafo import ler_grafo_arquivo

def calcular_caminhos_disjuntos_para_grafos():
    ## Arquivos gerados previamente com o gerar_grafos() que foi utilizado no TP01
    arquivos = [
        "Implementação 03/grafo_fortemente_conexo_10.txt", "Implementação 03/grafo_fortemente_conexo_100.txt",
        "Implementação 03/grafo_fortemente_conexo_1000.txt", "Implementação 03/grafo_fortemente_conexo_10000.txt",
        "Implementação 03/arvore_geradora_minima_10.txt", "Implementação 03/arvore_geradora_minima_100.txt", 
        "Implementação 03/arvore_geradora_minima_1000.txt", "Implementação 03/arvore_geradora_minima_10000.txt"
    ]
    
    origem, destino = 0, 1
    resultados = []

    for caminho_arquivo in arquivos:
        print(f"Processando {caminho_arquivo}...")
        
        start_time = time.perf_counter_ns()
        grafo, origem, destino = ler_grafo_arquivo(caminho_arquivo)
        caminhos_disjuntos = grafo.fluxo_maximo(origem, destino)
        end_time = time.perf_counter_ns()
        
        tempo_execucao_ms = (end_time - start_time) / 1_000_000  # Tempo em milissegundos
        resultados.append((caminho_arquivo, origem, destino, caminhos_disjuntos, tempo_execucao_ms))
        
        print(f"Arquivo: {caminho_arquivo}, Origem: {origem}, Destino: {destino}, Caminhos disjuntos: {caminhos_disjuntos}, Tempo de execução: {tempo_execucao_ms:.6f} ms")

    print("\nResultados Finais:\n")
    print("Arquivo".ljust(35) + "Origem".ljust(10) + "Destino".ljust(10) + "Caminhos Disjuntos".ljust(20) + "Tempo de Execução (ms)")

    for arquivo, origem, destino, caminhos, tempo in resultados:
        nome_arquivo_formatado = arquivo.replace("Implementação 03/", "").replace(".txt", "").strip()
        print(f"{nome_arquivo_formatado.ljust(35)}{str(origem).ljust(10)}{str(destino).ljust(10)}{str(caminhos).ljust(20)}{tempo:.6f}")


def main():
    calcular_caminhos_disjuntos_para_grafos()

if __name__ == "__main__":
    main()
