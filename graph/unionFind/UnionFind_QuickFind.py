class UnionFindNode:
    """Nodo di una struttura dati union-find."""
    def __init__(self, e):
        self.elem = e
        self.father = None
        self.sons = []

class UnionFindQuickFind:
    """Rappresenta una collezione di alberi QuickFind."""
    def __init__(self):
        self.nodes = []  # lista contenente tutti i nodi creati

    def makeset(self, e):
        """Crea un nuovo albero.

        L'albero sara' composto dal nodo contenente l'elemento passato come
        parametro piu' un nodo radice avente medesimo nome.
        """
        root = UnionFindNode(e)
        node = UnionFindNode(e)
        root.sons.append(node)
        node.father = root
        self.nodes.append(node)

    def find(self, node):
        return node.father.elem

    def union(self, rootA, rootB):
        if rootA == rootB:  # si vuole fondere lo stesso albero!
            return
        for sonB in rootB.sons:
            rootA.sons.append(sonB)
            sonB.father = rootA

def main():
    uf = UnionFindQuickFind()

    for i in range(10):
        print("makeset(" + str(i) + ")")
        uf.makeset(i)

    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 0 e l'albero"
    " contentente il nodo 2")
    uf.union(uf.nodes[0].father, uf.nodes[2].father)

    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 8 e l'albero"
    " contentente il nodo 4")
    uf.union(uf.nodes[8].father, uf.nodes[4].father)

    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 0 e l'albero"
    " contentente il nodo 8")
    uf.union(uf.nodes[0].father, uf.nodes[8].father)
    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 5 e l'albero"
    " contentente il nodo 8")
    uf.union(uf.nodes[5].father, uf.nodes[8].father)
    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

if __name__ == "__main__":
    main()
