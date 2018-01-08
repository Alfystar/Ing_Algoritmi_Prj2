from tree.binaryTree import BinaryTree
from tree.binaryTree import BinaryNode


class DictBinaryTree:
    """Un albero binario di ricerca e' un albero che soddisfa le seguenti proprieta':
    1. ogni nodo v contiene un valore (info[1]) cui e' associata una chiave (info[0])
        presa da n dominio totalmente ordinato.
    2. Le chiavi nel sottoalbero sinistro di v sono <= chiave(v).
    3. Le chiavi nel sottoalbero destro di v sono >= chiave(v)."""
    def __init__(self):
        self.tree = BinaryTree() # node's info now is a list [key, value]
    
    def key(self, node):
        """Permette di ritornare la chiave associata ad un nodo"""
        if node == None:
            return None
        return node.info[0]
    
    def value(self, node):
        """Permette di ritornare il valore associato ad un nodo"""
        if node == None:
            return None
        return node.info[1]
    
    def maxKeySon(self, root):
        """Permette di ottenere il nodo con chiave piu' grande,
        partendo dal nodo root. Il nodo con chiave
        piu' grande e' quello che si trova piu' a destra possibile"""
        curr = root
        while curr.rightSon != None:
            curr = curr.rightSon
        return curr
    
    def isLeftSon(self, node):
        """Permette di capire se il nodo node è il figlio sinistro del proprio
        padre."""
        if node == node.father.leftSon:
            return True
        return False
    
    def search(self, key):
        """Permette di ottenere il valore associato alla chiave key presente
        all'interno dell'albero"""
        node = self.searchNode(key)
        return self.value(node)
    
    def searchNode(self, key):
        """Permette di ricercare il nodo con chiave key all'interno del dizionario.
        Ritorna il nodo, oppure None se non c'è nodo associato a key"""
        if self.tree.root == None:
            return None
        
        curr = self.tree.root
        while curr != None:
            ck = self.key(curr)
            if key == ck:
                return curr
            
            if key < ck:
                curr = curr.leftSon
            else:
                curr = curr.rightSon
        
        return None
    
    def insert(self, key, value):
        """Permette di inserire un valore all'interno del dizionario
        nella maniera corretta"""
        pair = [key, value]
        newt = BinaryTree(BinaryNode(pair))
        
        if self.tree.root == None:
            self.tree.root = newt.root
        else:
            curr = self.tree.root #nodo corrente
            pred = None             #nodo precedente che abbiamo analizzato
            while curr != None:
                pred = curr
                if key <= self.key(curr): #chiave che sto inserendo e' piu piccola di quella corrente
                    curr = curr.leftSon
                else:
                    curr = curr.rightSon
            
            if key <= self.key(pred):
                self.tree.insertAsLeftSubTree(pred, newt)
            else:
                self.tree.insertAsRightSubTree(pred, newt)

    def cutOneSonNode(self, node): #contrai un nodo con un singolo figlio
        """Permette di cancellare un nodo dall'albero, sapendo che il nodo
        che si sta cancellando ha al massimo un solo figlio."""
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

    def delete(self, key):
        """Permette di cancellare il nodo appartenente all'albero con
        chiave key"""
        toRemove = self.searchNode(key)
        if toRemove != None:
            if toRemove.leftSon == None or toRemove.rightSon == None: #sto rimuovendo un nodo che ha 0 o 1 figlio
                self.cutOneSonNode(toRemove)
            else: # sto rimuovendo un nodo che ha due nodi figli
                maxLeft = self.maxKeySon(toRemove.leftSon) #predecessore del nodo da rimuovere
                toRemove.info, maxLeft.info = maxLeft.info, toRemove.info # scambio il contenuto informativo dei nodi
                self.cutOneSonNode(maxLeft) #adesso so che maxLeft non ha figli destri e posso applicare la cutOneSonNode

if __name__ == "__main__":
    diz = DictBinaryTree()
    
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
