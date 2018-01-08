from unionFind.UnionFind_QuickFind import UnionFindNode

class UnionFindQuickUnion:
    """ Rappresenta una collezione di alberi QuickUnion."""
    def __init__(self):
        self.nodes = []

    def makeset(self, e):
        """"Crea un albero di un solo nodo."""
        node = UnionFindNode(e)
        self.nodes.append(node)

    def findRoot(self, node):
        """Trova la radice dell'albero a cui appartiene questo nodo."""
        root = node
        while root.father != None:  # root non e' ancora la radice
            root = root.father
        return root

    def find(self, node):
        root = self.findRoot(node)
        return root.elem

    def union(self, rootA, rootB):
        """" Appende la radice di un albero alla radice dell'altro."""
        if rootA == rootB:
            return
        rootB.father = rootA

def main():
    uf = UnionFindQuickUnion()

    for i in range(10):
        print("makeset(" + str(i) + ")")
        uf.makeset(i)

    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 0 e l'albero"
    " contentente il nodo 2")
    uf.union(uf.findRoot(uf.nodes[0]), uf.findRoot(uf.nodes[2]))

    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 8 e l'albero"
    " contentente il nodo 4")
    uf.union(uf.findRoot(uf.nodes[8]), uf.findRoot(uf.nodes[4]))

    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 0 e l'albero"
    " contentente il nodo 8")
    uf.union(uf.findRoot(uf.nodes[0]), uf.findRoot(uf.nodes[8]))
    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

    print("union effettuata sull'albero contenete il nodo 5 e l'albero"
    " contentente il nodo 8")
    uf.union(uf.findRoot(uf.nodes[5]), uf.findRoot(uf.nodes[8]))
    for i in range(10):
        print("find(" + str(i) + ")= " + str(uf.find(uf.nodes[i])))

if __name__ == "__main__":
    main()

