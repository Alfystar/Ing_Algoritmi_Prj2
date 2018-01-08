class BinaryHeapNode:
    def __init__(self, e, k, i):
        self.elem = e
        self.key = k
        self.index = i

class PQbinaryHeap:
    def __init__(self):
        self.heap = []      #lista dif BinaryHeapNode
        self.length = 0

    def minSon(self, node):
        """Ricerca del figlio di chiave minima"""
        if node.index * 2 + 1 > self.length - 1:
            return None     #e' una foglia
        if node.index * 2 + 2 > self.length - 1:
            return self.heap[node.index * 2 + 1]    #ha un solo figlio
        if self.heap[node.index * 2 + 1].key < \
                self.heap[node.index * 2 + 2].key:
           return self.heap[node.index * 2 + 1]
        else:
            return self.heap[node.index * 2 + 2]

    def swap(self, node1, node2):
        self.heap[node1.index] = node2
        self.heap[node2.index] = node1
        node1.index, node2.index = node2.index, node1.index

    def moveUp(self, son):
        if son.index <= 0:
            return
        father = self.heap[(son.index - 1) // 2]
        while son.index > 0 and son.key < father.key:
            self.swap(son, father)
            father = self.heap[(son.index - 1) // 2]

    def moveDown(self, father):
        son = self.minSon(father)
        while son != None and son.key < father.key:
            self.swap(father, son)
            son = self.minSon(father)

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def popMin(self):
        pq_node = self.findMin()
        self.deleteMin()
        return pq_node

    def findMin(self):
        if self.isEmpty():
            return None
        return self.heap[0].elem

    def insert(self, e, k):
        n = BinaryHeapNode(e, k, self.length)
        if self.length < len(self.heap):
            self.heap[self.length] = n
        else:
            self.heap.append(n)
        self.length += 1
        self.moveUp(n)
        return n

    def deleteMin(self):
        if self.length == 0:
            return
        first = self.heap[0]
        last = self.heap[self.length - 1]
        self.swap(first, last)
        self.length -= 1
        self.moveDown(last)
        #del self.heap[self.length]

    def decreaseKey(self, node, nKey):
        node.key = nKey
        self.moveUp(node)

    def stampa(self):
        s = ""
        for i in range(self.length):
            n=self.heap[i]
            s += "[{},{}] ".format(n.elem, n.key)
        print( s)

def main():
    pq = PQbinaryHeap()
    if pq.isEmpty():
        print( "Empty queue")
    e = 4.0
    k = 2.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print( "findMin():", pq.findMin())

    e = 2.0
    k = 1.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print( "findMin():", pq.findMin())

    e = 8.0
    k = 4.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print( "findMin():", pq.findMin())

    e = 10.0
    k = 5.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print( "findMin():", pq.findMin())

    e = 6.0
    k = 3.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print( "findMin():", pq.findMin())

    print( "deleteMin()")
    pq.deleteMin()
    pq.stampa()
    print( "findMin():", pq.findMin())

    e = 12.0
    k = 6.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()

    e = 14.0
    k = 7.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()

    e = 16.0
    k = 8.0
    print( "insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()

    print( "deleteMin()")

    pq.deleteMin()
    pq.stampa()

if __name__ == "__main__":
    main()
