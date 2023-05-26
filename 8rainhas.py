import networkx as nx
import random

G = nx.read_gml("incompatibilidades.gml", label = 'label')
possiveisCasas = []
solucao = []
adjacente = True

while(len(solucao) < 8):
    solucao.clear()
    
    for x in G.nodes:
        possiveisCasas.append(int(x))

    while(len(possiveisCasas) > 0):
        casa = int(random.choice(possiveisCasas))
        
        if len(solucao) == 0:
            solucao.append(casa)
        else:
            for x in solucao:
                for y in G.edges:
                    if (int(y[0]) == casa and int(y[1]) == x) or (int(y[0]) == x and int(y[1]) == casa):
                        adjacente = False
                        possiveisCasas.remove(casa)
                        break
                    else:
                        adjacente = True
                
                if(adjacente == False):
                    break
                        
        if adjacente == True:
            if casa not in solucao:
                solucao.append(casa)
            possiveisCasas.remove(casa)

print(f'Conjunto independente: {solucao}')
print()
print('TABULEIRO:')

coluna = linha = 0

for x in range(8):
    if coluna in solucao:
        print("R  ", end="")
    else:
        print("X  ", end="")
    
    for y in range(7):
        linha += 8
        
        if linha in solucao:
            print("R  ", end="")
        else:
            print("X  ", end="")
    
    print()
    coluna += 1
    linha = coluna