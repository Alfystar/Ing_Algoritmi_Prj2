if __name__ == '__main__':
    from makeGraph.creaGrafo import mkGraph


def medNode(G, node):
    sonBranch = G.getAdjList(node.id)  # lista contenente i figli
    print(sonBranch)
    c = pathsCountLevel(sonBranch)
    print("numero percorsi:{}".format(c))


def pathsCountLevel(sonLevel):
    """
    funzione che calcola per un certo livello quanti cammini non doppi si possono fare
    che passano per il nodo originale NODE
    :param sonLevel: lista di lista dove ogni lista contiene i discendenti dei primi figli di NODE, NESSUNA LISTA VUOTA
    :return: numero di percorsi
    """
    count = 0
    allNode = 0
    print("figli nel livello:{}".format(sonLevel))
    for i in sonLevel:  # tutti i figli nei vari sotto blocchi
        if (type(i) == int):
            allNode += 1
        else:
            allNode += len(i)

    print("nodi presenti:{}".format(allNode))

    for i in range(len(sonLevel)):
        if (type(sonLevel[i]) == int):
            count += (allNode - 1)    # caso particolare 1*(allNode - 1)
            allNode -= 1
        else :
            count += len(sonLevel[i]) * (allNode - len(sonLevel[i]))
            allNode -= len(sonLevel[i])
    return count


if __name__ == '__main__':
    print("funzione per trovare quante volte il nodo n è medio in G")
    i = mkGraph(10, 2, "star")
    listNode = i.getNodes()
    i.print()
    medNode(i, listNode[0])
