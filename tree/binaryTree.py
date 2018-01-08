if __name__ == '__main__':
    from stack.Stack import PilaArrayList
    from queue.Queue import CodaArrayList_deque
else:
    from stack.Stack import PilaArrayList
    from queue.Queue import CodaArrayList_deque

class BinaryNode:
    def __init__(self, info):
        self.info = info
        self.father = None
        self.leftSon = None
        self.rightSon = None

class BinaryTree:
    def __init__(self, rootNode=None):
        self.root = rootNode
    
    def insertAsLeftSubTree(self, father, subtree):
        """Permette di inserire la radice di un sottoalbero come figlio sinistro
        del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.leftSon = son
    
    def insertAsRightSubTree(self, father, subtree):
        """Permette di inserire la radice di un sottoalbero come figlio destro
        del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.rightSon = son

    def cutLeft(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte dal figlio
        sinistro del nodo father"""
        son = father.leftSon
        newTree = BinaryTree(son)
        father.leftSon = None
        return newTree
    
    def cutRight(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte dal figlio
        destro del nodo father"""
        son = father.rightSon
        newTree = BinaryTree(son)
        father.rightSon = None
        return newTree

    def DFS(self):
        """Permette di restituire una lista di elementi ottenuta da una visita
        in profondità dell'albero."""
        res = []     
        stack = PilaArrayList()
        if self.root != None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            res.append(current.info)
            if current.rightSon != None:
                stack.push(current.rightSon)
            if current.leftSon != None:
                stack.push(current.leftSon)
        return res

    def BFS(self):
        """Permette di restituire una lista di elementi ottenuta da una visita
        in ampiezza dell'albero."""
        res = []
        q = CodaArrayList_deque()
        if self.root != None:
            q.enqueue(self.root)
        while not q.isEmpty():
            current = q.dequeue()
            res.append(current.info)
            if current.leftSon != None:
                q.enqueue(current.leftSon)
            if current.rightSon != None:
                q.enqueue(current.rightSon)
        return res

    def cut(self, node):
        """Stacca e restituisce l'intero sottoalbero radicato in node. L'operazione
        cancella dall'albero il nodo node e tutti i suoi discendenti."""
        if node == None:
            return BinaryTree(None)
        if node.father == None: #nodo radice
            self.root = None
            return BinaryTree(node)
        f = node.father
        if node.leftSon == None and node.rightSon == None: #a leaf!
            if f.leftSon == node:
                f.leftSon = None
            else:
                f.rightSon = None
            return BinaryTree(node)
        elif f.leftSon == node:
            nt = self.cutLeft(f)
            #f.leftSon = None  --> Questa operazione viene fatta in cutLeft
            return nt
        else:
            nt = self.cutRight(f)
            #f.rightSon = None  --> Questa operazione viene fatta in cutRight
            return nt

    def stampa(self):
        """Permette di stampare l'albero. Per farlo si usa una pila di appoggio"""
        stack = PilaArrayList()
        if self.root != None:
            stack.push([self.root, 0]) #pila di liste di due elementi [il nodo, il livello occupato dal nodo]
        else:
            print("Empty tree!")
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            print("|---"*level + str(current[0].info))
            
            if current[0].rightSon != None:
                stack.push([current[0].rightSon, level + 1])
            if current[0].leftSon != None:
                stack.push([current[0].leftSon, level + 1])


if __name__ == "__main__":
        print("alb1=nodo1=1")
        alb1 = BinaryTree(BinaryNode(1))
        nodo1 = alb1.root

        print("alb2=nodo2=2")
        alb2 = BinaryTree(BinaryNode(2))
        nodo2 = alb2.root

        print("alb3=nodo3=3")
        alb3 = BinaryTree(BinaryNode(3));
        nodo3 = alb3.root

        print("alb4=nodo4=4")
        alb4 = BinaryTree(BinaryNode(4))
        nodo4 = alb4.root

        print("alb5=nodo5=5")
        alb5 = BinaryTree(BinaryNode(5))
        nodo5 = alb5.root
        
        print("alb6=nodo6=6")
        alb6 = BinaryTree(BinaryNode(6))
        nodo6 = alb6.root

        print("alb1.innestaDestro(nodo1,alb3)")
        alb1.insertAsRightSubTree(nodo1, alb3)
        print("alb1.innestaSinistro(nodo1,alb2)")
        alb1.insertAsLeftSubTree(nodo1, alb2)
        print("alb1.innestaDestro(nodo3,alb4)")
        alb1.insertAsLeftSubTree(nodo3, alb4)
        print("alb1.innestaSinistro(nodo2,alb5)")
        alb1.insertAsLeftSubTree(nodo2, alb5)
        print("alb1.innestaDestro(nodo2,alb6)")
        alb1.insertAsRightSubTree(nodo2, alb6)

        alb1.stampa()
        alb1.cut(nodo2)
        alb1.stampa()
        print("alb1.DFS()")
        visita = alb1.DFS()
        print(visita)

        print("alb1.BFS()")
        visita = alb1.BFS()
        print(visita)

        print("alb8=alb1.cutLeft(nodo2)")
        alb8 = alb1.cutLeft(nodo2)
        print("alb1.DFS()")
        visita = alb1.DFS()
        print(visita)
        print("alb8.DFS()")
        visita = alb8.DFS()
        print(visita)
