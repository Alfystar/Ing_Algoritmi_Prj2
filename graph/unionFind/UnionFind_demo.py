from UnionFind_QuickFind import UnionFindQuickFind
from UnionFind_BalancedQuickFind import UnionFindBalancedQuickFind
from UnionFind_QuickUnion import UnionFindQuickUnion
from UnionFind_BalancedQuickUnion import UnionFindBalancedQuickUnion
from UnionFind_QuickUnion_PathCompression import UnionFindQuickUnionPathCompression
from random import random
from random import randint
from time import time

def testUnionFind(amount,nCalls,pFind,simple):
    """Definisce un test sulle diverse strutture union-find.

    Verra' eseguito un numero totale di chiamate pari a 'nCalls' suddivise tra
    union e find in base al parametro 'pFind' che dara' la probabilita' che si
    effettui una find invece che una union. 'amount' indica il valore massimo
    assegnato ad ogni nodo. 'simple' e' un flag per indicare se si vogliono
    svolgere o meno tali operazioni anche su strutture union-find di base,
    ovvero UnionFind_QuickFind e UnionFindQuickUnion.
    """
    sequence=[]  # conterra' le operazioni da svolgere indicate tramite una
                 # tupla del tipo (f, i), ovvero trova il nodo i
                 # oppure (u, n1, n2), ovvero union alberi contenenti n1 e n2
    for _ in range(nCalls):
        choice=random()
        if choice<=pFind:
            n=randint(0,amount-1)
            sequence.append(('f',n))
        else:
            n1=randint(0,amount-1)
            n2=n1
            while n2==n1:
                n2=randint(0,amount-1)
            sequence.append(('u',n1,n2))

    if simple:
        print("UnionFindQuickFind")
        uf=UnionFindQuickFind()
        for i in range(amount):
            uf.makeset(i)
        start=time()
        for s in sequence:
            if s[0]=='f':
                uf.find(uf.nodes[s[1]])
            else:
                uf.union(uf.nodes[s[1]], uf.nodes[s[2]])
        elapsed=time()-start
        print("Sequence of {} calls over {} elements with Find probability {}"\
            " took {:.5f} seconds.\n".format(nCalls,amount,pFind,elapsed))

    print("UnionFindQuickFind bilanciato")
    uf=UnionFindBalancedQuickFind()
    for i in range(amount):
        uf.makeset(i)
    start=time()
    for s in sequence:
        if s[0]=='f':
            uf.find(uf.nodes[s[1]])
        else:
            uf.union(uf.nodes[s[1]], uf.nodes[s[2]])
    elapsed=time()-start
    print("Sequence of {} calls over {} elements with Find probability {} "\
            "took {:.5f} seconds.\n".format(nCalls,amount,pFind,elapsed))

    if simple:
        print("UnionFindQuickUnion")
        uf=UnionFindQuickUnion()
        for i in range(amount):
            uf.makeset(i)
        start=time()
        for s in sequence:
            if s[0]=='f':
                uf.find(uf.nodes[s[1]])
            else:
                uf.union(uf.findRoot(uf.nodes[s[1]]), \
                        uf.findRoot(uf.nodes[s[2]]))
        elapsed=time()-start
        print("Sequence of {} calls over {} elements with Find probability {}"\
                " took {:.5f} seconds.\n".format(nCalls,amount,pFind,elapsed))

    print("UnionFindQuickUnion bilanciato")
    uf=UnionFindBalancedQuickUnion()
    for i in range(amount):
        uf.makeset(i)
    start=time()
    for s in sequence:
        if s[0]=='f':
            uf.find(uf.nodes[s[1]])
        else:
            uf.union(uf.findRoot(uf.nodes[s[1]]), uf.findRoot(uf.nodes[s[2]]))
    elapsed=time()-start
    print("Sequence of {} calls over {} elements with Find probability {} "\
            "took {:.5f} seconds.\n".format(nCalls,amount,pFind,elapsed))

    print("UnionFindQuickUnion pathCompression")
    nodes=[]
    uf=UnionFindQuickUnionPathCompression()
    for i in range(amount):
        uf.makeset(i)
    start=time()
    for s in sequence:
        if s[0]=='f':
            uf.find(uf.nodes[s[1]])
        else:
            uf.union(uf.findRoot(uf.nodes[s[1]]), uf.findRoot(uf.nodes[s[2]]))
    elapsed=time()-start
    print("Sequence of {} calls over {} elements with Find probability {} "\
            "took {:.5f} seconds.\n".format(nCalls,amount,pFind,elapsed))

if __name__ == '__main__':
    testUnionFind(10000,10000,0.75,True)
    print(10*' '+30*'*'+'\n')
    testUnionFind(10000,10000,0.5,True)
    print(10*' '+30*'*'+'\n')
    testUnionFind(10000,10000,0.25,True)
    print(10*' '+30*'*'+'\n')
    print(10*' '+30*'*'+'\n')
    testUnionFind(100000,100000,0.75,False)
    print(10*' '+30*'*'+'\n')
    testUnionFind(100000,100000,0.5,False)
    print(10*' '+30*'*'+'\n')
    testUnionFind(100000,100000,0.25,False)

