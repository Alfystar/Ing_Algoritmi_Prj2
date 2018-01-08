from list.LinkedList import ListaCollegata


class DictionaryUnorderedLinkedList:
    """
    Dizionario che mantiene una lista disordinata di coppie chiave valore.
    Ha le seguenti caratteristiche:
    - Inserimento degli elementi in O(1)
    - Ricerca di un elemento in O(n)
    - Cancellazione di un elemento in O(n)
    """

    def __init__(self):
        self.theList = ListaCollegata()
    
    def search(self, k):
        current = self.theList.first
        while current != None:
            currkey = current.elem[0]
            if currkey == k:
                break
            current = current.next
        else:
            return None
        
        return current.elem[1]
    
    #very fast!
    def insert(self, key, value):
        pair = [key, value]
        self.theList.addAsLast(pair)
    
    def delete(self, key):
        current = self.theList.first
        pred = None
        while current != None:
            currkey = current.elem[0]
            if currkey == key:
                break
            pred = current
            current = current.next
        else:
            return None
        
        if pred == None:
            self.theList.popFirst()
        else:
            pred.next = current.next

if __name__ == "__main__":
    print("Dictionary (unordered linked list).")
    d = DictionaryUnorderedLinkedList()
    print("insert({},{})".format(0, 10))
    d.insert(0, 10)
    print("insert({},{})".format(2, 12))
    d.insert(2, 12)
    print("insert({},{})".format(1, 11))
    d.insert(1, 11)
    print("insert({},{})".format(8, 18))
    d.insert(8, 18)
    print("insert({},{})".format(5, 15))
    d.insert(5, 15)
    
    d.theList.stampa()
    
    print("delete({})".format(0))
    d.delete(0)
    
    d.theList.stampa()
    
    print("search({})".format(5))
    print(d.search(5))
