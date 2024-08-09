#Implementação do método Forward Start

def forward_star(arcOrig, arcDest, pointer, vertice):
    
    grau_entrada = grau_saida = 0
    sucessores = []
    predecessores = []
    
    posicao = pointer[vertice-1]
    grau_saida = pointer[vertice] - pointer[vertice-1]
        
    for i in range(len(arcDest)):
        if(arcDest[i] == vertice):
            grau_entrada += 1
            predecessores.append(arcOrig[i])
        
    for i in range(grau_saida):
        sucessores.append(arcDest[posicao + i])
    
    return grau_saida, grau_entrada, sucessores, predecessores