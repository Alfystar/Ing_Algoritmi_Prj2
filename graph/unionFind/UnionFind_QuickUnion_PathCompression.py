from unionFind.UnionFind_BalancedQuickUnion import UnionFindBalancedQuickUnion

class UnionFindQuickUnionPathCompression(UnionFindBalancedQuickUnion):
    """Union-find con bilanciamento e compressione.

    Durante le find() utilizza l'euristica di path compression.
    Si eseguono n makeset, m find ed al piu' (n-1) union in tempo
    O(n+m*a(m+n,n)), dove 'a' e' l'inversa della funzione di Ackermann e
    presenta una crescita ancora piu' lenta della funzione log* [vedi cap.9.4.3
    del libro di testo].
    """

    def findRoot(self, node):
        """Trova la radice dell'albero e comprimi.

        Ogni nodo incontrato fino alla radice diventa figlio diretto di essa.
        """
        relatives = []
        root = node
        while root.father != None:
            relatives.append(root)  #colleziona tutti i nodi incontrati
            root = root.father
        for node in relatives[:-1]:  #collega tutti alla radice tranne l'ultimo
            node.father = root
            root.sons.append(node)
        return root

def main():
    uf = UnionFindQuickUnionPathCompression()

    for i in range(10):
        print("makeset(" + str(i) + ")")
        root = uf.makeset(i)

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
