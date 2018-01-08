from unionFind.UnionFind_QuickFind import UnionFindNode, UnionFindQuickFind

class UnionFindNodeBalanced(UnionFindNode):
    def __init__(self, e):
        super().__init__(e)  #con python < 3 usare: 
                             #super(UnionFindBalancedNode,self).__init__(e)
        self.size = 1  #nuovo attributo, rappresenta la dimensione dell'albero

#Come UnionFindQuickUnion, ma con union bilanciata per size
class UnionFindBalancedQuickFind(UnionFindQuickFind):

    def makeset(self, e):
        root = UnionFindNodeBalanced(e)
        son = UnionFindNodeBalanced(e)
        root.sons.append(son)
        son.father = root
        self.nodes.append(son)

    def union(self, rootA, rootB):
        """La radice con meno figli cede i propri figli all'altra radice"""
        if rootA == rootB:
            return rootA

        if rootA.size >= rootB.size:
            for sonB in rootB.sons:
                sonB.father = rootA
                rootA.sons.append(sonB)
            rootA.size += rootB.size
        else:
            for sonA in rootA.sons:
                sonA.father = rootB
                rootB.sons.append(sonA)
            rootB.size += rootA.size

def main():
    uf = UnionFindBalancedQuickFind()

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
