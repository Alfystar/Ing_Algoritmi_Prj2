from unionFind.UnionFind_BalancedQuickFind import UnionFindNodeBalanced
from unionFind.UnionFind_QuickUnion import UnionFindQuickUnion

class UnionFindBalancedQuickUnion(UnionFindQuickUnion):
    """Rappresenta una collezione di alberi bilanciati QuickUnion."""

    def makeset(self, e):
        """Crea un albero con un solo nodo"""
        node = UnionFindNodeBalanced(e)
        self.nodes.append(node)

    def union(self, rootA, rootB):
        """Appende la radice di un albero alla radice dell'altro"""
        if rootA == rootB:
            return
        if rootA.size >= rootB.size:
            rootA.size += rootB.size
            rootB.father = rootA
        else:
            rootB.size += rootA.size
            rootA.father = rootB

def main():
    uf = UnionFindBalancedQuickUnion()

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
