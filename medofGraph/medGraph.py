from makeGraph.creaGrafo import mkGraph
from medOfNode.medNode import medNode

debug = False

def mostNodes(grafo):
    """
    La funzione scorre tutti i nodi meno quelli fogli e su di essi esegue medNode, per scoprire quante volte è medio
    :param grafo:
    :return:
    """
    listNode = grafo.getNodes()
    maxMed = [[None, 0]]
    for node in listNode:
        if len(grafo.getAdj(node.id)) == 1:
            if (debug): print("dentro if per nodo {}".format(node.id))
            continue
        else:
            if (debug): print("dentro else per nodo {}".format(node.id))
            med = medNode(grafo, node)
            maxMed = findBetterNode(med, node, maxMed)
    return maxMed

def findBetterNode(numMed, node, savedNode):
    """
    salva nodo e quante volte è medio solo se è maggiore o uguale di quello attuale
    :param numMed:
    :return:
    """
    if (type(savedNode[0][0]) == None or savedNode[0][1] < numMed):
        savedNode = [[node, numMed]]
    elif savedNode[0][1] == numMed:
        savedNode.append([node, numMed])
    return savedNode


if __name__ == '__main__':
    g = mkGraph(2000, "rand", 500)

    listaNodi = mostNodes(g)

    print("Nodo/i medi per piu' volte:\n")

    for elem in listaNodi:
        print("Nodo {} medio per {} volte.\n".format(elem[0].id, elem[1]))
