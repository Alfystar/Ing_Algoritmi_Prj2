from stack.Stack import PilaArrayList
from queue.Queue import CodaArrayList_deque

class TreeArrayListNode:
    def __init__(self, info):
        self.info = info
        self.father = None
        self.sons = []

class TreeArrayList:

    def __init__(self, rootNode=None):
        self.root = rootNode
        
    def insert(self, father, sonsTree):
        sonsTree.root.father = father
        father.sons.append(sonsTree.root)

    def cut(self, node):
        if node.father == None: #it is the root
            return self
        
        try:
            node.father.sons.remove(node)
        except ValueError:
            raise Exception("Error: unable to find the selected son to cut away!")
        
        node.father = None
        return TreeArrayList(node)
    
    def DFS(self):
        res = []     
        stack = PilaArrayList()
        if self.root is not None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            res.append(current.info)
            for i in range(len(current.sons) - 1, -1, -1):
                stack.push(current.sons[i])
        return res

    def BFS(self):
        res = []
        q = CodaArrayList_deque()
        if self.root is not None:
            q.enqueue(self.root)
        while not q.isEmpty():
            current = q.dequeue()
            res.append(current.info)
            for s in current.sons:
                q.enqueue(s)
        return res

    def foundNodeByElem(self, elem):
        """Visita DFS per cercare un nodo che contenga l'indice richiesto."""
        stack = PilaArrayList()
        if self.root != None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            if elem == current.info:
                return current
            for i in range(len(current.sons)):
                stack.push(current.sons[i])
        return None

