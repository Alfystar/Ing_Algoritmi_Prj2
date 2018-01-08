if __name__ == '__main__':
    from makeGraph.creaGrafo import mkGraph


def medNode(G, node):
    sonBranch = G.getAdjList(node.id)  # lista contenente i figli
    #listNode = G.getNodes()
    print("figli nel primo livello:[{}".format(sonBranch))
    count = 0
    ramo=[]
    while(len(sonBranch)>=2):          #procedo finche almeno 2 rami del nodo origine hanno dei figli
        count += pathsCountLevel(sonBranch) #ottengo le coppie per questo livello
        for i in range(len(sonBranch)): #ottengo il nuovo livello da calcolare
            ramo=(sonBranch.pop())
            newSonBranch=[]
            idDad = ramo[i]
            for i in range(len(ramo)):
                newSonBranch.extend(hisSon(G,idDad,ramo[i]))

    print("numero percorsi:{}".format(count))

    return count

def sonNextLevel(G,ramiAttuali)


# hisSon(G, listNode[0], listNode[1])


def hisSon(G,nodeDad,node):
    """
    Funzione che ritorna tutti i filgli di un nodo sapendo chi era suo padre
    e quindi evitando di riprenderlo
    :param G: grafo
    :param nodeDad: padre del nodo di cui sapere figli
    :param node: nodo per i quali siamo interessati ad avere i figli
    :return: lista dei suoi nodi figli(sotto forma di id) eslusi suo padre
    """
    son=G.getAdj(node.id,nodeDad.id)
    #print("figli del nodo {} provenienti dal nodo {} sono:{}".format(node.id,nodeDad.id,son))
    return son


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
            count += (allNode - 1)  # caso particolare 1*(allNode - 1)
            allNode -= 1
        else:
            count += len(sonLevel[i]) * (allNode - len(sonLevel[i]))
            allNode -= len(sonLevel[i])
    return count


if __name__ == '__main__':
    print("funzione per trovare quante volte il nodo n è medio in G")
    i = mkGraph(55, 15)
    listNode = i.getNodes()
    i.print()
    medNode(i, listNode[0])
