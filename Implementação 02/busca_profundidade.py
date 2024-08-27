# Implementação do método Busca Profundidade
#  vetor_vertices_origem[1][0]['vertice_saida']

def busca_profundidade(v, tempo):
    global vetor_vertices_origem, tempoDescoberta, tempoTermino, arestasArvore, arestasRetorno

    tempo = tempo + 1
    tempoDescoberta[v] = tempo
    
    for vertice in vetor_vertices_origem:
        if tempoDescoberta[v] is None:
            arestasArvore.append((vertice[v]['vertice_origem'], vertice[v]['vertice_saida']))
            busca_profundidade(v)
        elif (tempoTermino[v] is None) and ():
            arestasRetorno.append((vertice[v]['vertice_origem'], vertice[v]['vertice_saida']))
            
        tempoTermino = tempo

    # Retorna um valor arbitrário apenas para exemplo
    return 100

