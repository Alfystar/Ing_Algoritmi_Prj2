from medofGraph.medGraph import findBetterNode
from makeGraph.creaGrafo import grafoEsempio
from medOfNode.medNode import medNode



def main ():
    g=grafoEsempio()
    print("Il grafo in Fig1 ha la seguente matrice di adiacenza:")
    g.print()

    maxMed,lMed=listaMedi(g)

    print("\nNel grafo in Fig1 il nodo medio di più percorsi è:")   #funzione persa a demo main, non è escluso che ci siano più medi
    for elem in maxMed:
        print("\tNodo {} medio per {} volte.".format(elem[0].id, elem[1]))

    print("\nI singoli nodi sono medi:")
    for elem in lMed:
        print("\tNodo {} medio per {} volte.".format(elem[0].id, elem[1]))




def listaMedi(grafo):
    """
    :param grafo:
    :return:
    """
    listNode = grafo.getNodes()
    maxMed = [[None, 0]]
    listMed=[]
    for node in listNode:
        if len(grafo.getAdj(node.id)) == 1:
            listMed.append([node,0])
            continue
        else:
            med = medNode(grafo, node)
            listMed.append([node,med])
            maxMed = findBetterNode(med, node, maxMed)
    return maxMed, listMed



if __name__ == '__main__':
    main()
