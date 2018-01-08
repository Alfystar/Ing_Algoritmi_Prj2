if __name__ == '__main__':
    from makeGraph import creaGrafo

def medNode(G,node):
    sonBranch=G.getAdj(node.id)   #lista contenente i figli





def pathsCountLevel(sonLevel):
    """
    funzione che calcola per un certo livello quanti cammini non doppi si possono fare
    che passano per il nodo originale NODE
    :param sonLevel: lista di lista dove ogni lista contiene i discendenti dei primi figli di NODE
    :return: numero di percorsi
    """
    count=0
    allNode=0
    for i in sonLevel:  #tutti i figli nei vari sotto blocchi
        allNode+=len(i)
    for i in range(len(sonLevel)):
        count=len(sonLevel[i])*(allNode-len(sonLevel[i]))
        allNode-=len(sonLevel[i])
    return count


if __name__ == '__main__':
    print("funzione per trovare quante volte il nodo n è medio in G")
    i=creaGrafo("rand",10,2)