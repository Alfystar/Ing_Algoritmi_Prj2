from dictionary.dictTrees.trees.treeArrayList import TreeArrayList
from dictionary.dictTrees.trees.strutture.Stack import PilaArrayList


class Tree(TreeArrayList):

    def foundNodeByIndex(self, index):
        """Visita DFS per cercare un nodo che contenga l'indice richiesto."""
        stack = PilaArrayList()
        if self.root != None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            if index == current.info.index:
                return current
            for i in range(len(current.sons)):
                stack.push(current.sons[i])
        return None
