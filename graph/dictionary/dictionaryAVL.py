from dictBinaryTree import DictBinaryTree
from tree.binaryTree import BinaryNode
from tree.binaryTree import BinaryTree


class DictAVL(DictBinaryTree):
    def __init__(self):
        self.tree=BinaryTree()  #Node's info now is a triple [key,value,height]
    
    def height(self,node):
        """Restituisce l'altezza del sottoalbero che ha come radice node.
        Ovvero il numero di livelli di discendenza di quel nodo."""
        if node==None:
            return -1 #aiuta a calcolare il balance factor
        return node.info[2]
    
    def setHeight(self,node,h):
        """Metodo per settare l'altezza del nodo node al valore h."""
        if node!=None:
            node.info[2]=h
    
    def balanceFactor(self,node):
        """Permette di calcolare il fattore di bilanciamento del nodo node."""
        if node==None:
            return 0
        return self.height(node.leftSon) - self.height(node.rightSon)

    def updateHeight(self,node):
        """Permette di aggiornare l'altezza del nodo node al valore uguale a:
        massima altezza tra le altezza dei due figli, a cui deve essere aggiunto 1."""
        if node!=None:
            self.setHeight(node,max(self.height(node.leftSon),self.height(node.rightSon))+1)

# Balancing

    def rightRotation(self,node):
        leftSon = node.leftSon
        node.info,leftSon.info = leftSon.info,node.info
        
        rtree = self.tree.cutRight(node)
        ltree = self.tree.cutLeft(node)
        ltree_l = ltree.cutLeft(leftSon)
        ltree_r = ltree.cutRight(leftSon)
        
        ltree.insertAsRightSubTree(ltree.root, rtree)
        ltree.insertAsLeftSubTree(ltree.root, ltree_r)
        self.tree.insertAsRightSubTree(node, ltree)
        self.tree.insertAsLeftSubTree(node, ltree_l)
        
        self.updateHeight(node.rightSon)
        self.updateHeight(node)
    
    def leftRotation(self,node):
        rightSon=node.rightSon        
        node.info,rightSon.info=rightSon.info,node.info
        
        rtree=self.tree.cutRight(node)
        ltree=self.tree.cutLeft(node)
        rtree_l=rtree.cutLeft(rightSon)
        rtree_r=rtree.cutRight(rightSon)
        
        rtree.insertAsLeftSubTree(rtree.root, ltree)
        rtree.insertAsRightSubTree(rtree.root, rtree_l)
        self.tree.insertAsLeftSubTree(node, rtree)
        self.tree.insertAsRightSubTree(node, rtree_r)
        
        self.updateHeight(node.leftSon)
        self.updateHeight(node)

    def rotate(self,node):
        """Partendo dal nodo node, riesce a capire quale e' il tipo
        di rotazione da effettuare in base al fattore di bilanciamento
        del nodo e de suoi figli."""
        balFact=self.balanceFactor(node)
        if balFact==2: #altezza figlio sinistro di node e' piu' grande di 2 rispetto al figlio destro
            if self.balanceFactor(node.leftSon)>=0: #sbilanciamento SS
                self.rightRotation(node)
            else: #sbilanciamento SD
                self.leftRotation(node.leftSon)
                self.rightRotation(node)
        elif balFact==-2: #altezza figlio destro di node e' piu' grande di 2 rispetto al figlio sinistro
            if self.balanceFactor(node.rightSon)<=0: #sbilanciamento DD
                self.leftRotation(node)
            else: #sbilanciamento DS
                self.rightRotation(node.rightSon)
                self.leftRotation(node)
        
#INSERTION: quite the same as for dictBinaryTree. We have only to add the ability to manage nodes' height.

    def balInsert(self,newNode):
        curr=newNode.father
        while curr!=None:
            if abs(self.balanceFactor(curr))>=2:
                break #stop the height update at the first unbalanced predecessor.
            else:
                self.updateHeight(curr)
                curr=curr.father
        if curr!=None:
            self.rotate(curr)
    
    def insert(self, key, value):
        newt = BinaryTree(BinaryNode([key,value,0]))    #Primo cambiamento e' tripletta al posto della coppia key value
        
        if self.tree.root == None:
            self.tree.root = newt.root
        else:
            curr = self.tree.root
            pred = None
            while curr != None:
                pred = curr
                if key <= self.key(curr):
                    curr = curr.leftSon
                else:
                    curr = curr.rightSon
            
            if key <= self.key(pred):
                self.tree.insertAsLeftSubTree(pred, newt)
            else:
                self.tree.insertAsRightSubTree(pred, newt)
            self.balInsert(newt.root)                   #secondo cambiamento e' la chiamata del metodo per bilanciare l'albero

#DELETION: quite the same as for dictBinaryTree. We have only to add the ability to manage nodes' height.
    def balDelete(self,removedNode):
        curr=removedNode.father
        while curr!=None: #more than one may need to be rebalanced
            if abs(self.balanceFactor(curr))==2:
                self.rotate(curr)
            else:
                self.updateHeight(curr)
            curr=curr.father
    
    def cutOneSonNode(self, node): #contrai un nodo con un singolo figlio
        son = None
        if node.leftSon != None:
            son = node.leftSon
        elif node.rightSon != None:
            son = node.rightSon
        
        if son == None:
            self.tree.cut(node) #is a leaf
        else:
            node.info, son.info = son.info, node.info #swap info
            nt = self.tree.cut(son)
            self.tree.insertAsLeftSubTree(node, nt.cut(son.leftSon))
            self.tree.insertAsRightSubTree(node, nt.cut(son.rightSon))
        
        self.balDelete(node)    #This is the only change

    def delete(self, key):
        toRemove = self.searchNode(key)
        if toRemove != None:
            if toRemove.leftSon == None or toRemove.rightSon == None:
                self.cutOneSonNode(toRemove)
            else:
                maxLeft = self.maxKeySon(toRemove.leftSon)
                toRemove.info, maxLeft.info = maxLeft.info, toRemove.info
                #Avendo effettuato lo swap di tutto il campo info, si sono scambiate
                #anche le altezze dei nodi che invece dovevano rimanere uguali a prima
                #per tale motivo con queste tre righe di codice si ripristinano le
                #corrette altezze
                th=self.height(toRemove)
                self.setHeight(toRemove, self.height(maxLeft))
                self.setHeight(maxLeft, th)
                
                self.cutOneSonNode(maxLeft)

if __name__ == "__main__":
    diz = DictAVL()
    
    print("insert(6,12)")
    diz.insert(6, 12)
    diz.tree.stampa()
    
    print("insert(4,8)")
    diz.insert(4, 8)
    diz.tree.stampa()
    
    print("insert(3,6)")
    diz.insert(3, 6)
    diz.tree.stampa()
    
    print("insert(2,4)")
    diz.insert(2, 4)
    diz.tree.stampa()
    
    print("insert(1,2)")
    diz.insert(1, 2)
    diz.tree.stampa()
    
    print("insert(5,10)")
    diz.insert(5, 10)
    diz.tree.stampa()
    
    print("insert(7,14)")
    diz.insert(7, 14)
    diz.tree.stampa()
    
    print("search(5)=" + str(diz.search(5)))
    print("search(3)=" + str(diz.search(3)))
    print("search(6)=" + str(diz.search(6)))
    print("search(8)=" + str(diz.search(8)))
    
    print("delete(6)")
    diz.delete(6)
    diz.tree.stampa()
    
    print("delete(3)")
    diz.delete(3)
    diz.tree.stampa()
    
    print("delete(1)")
    diz.delete(1)
    diz.tree.stampa()
    
    print("delete(8)")
    diz.delete(8)
    diz.tree.stampa()