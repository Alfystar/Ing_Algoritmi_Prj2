from list import LinkedList


class DoubleRecord(LinkedList.Record):

    def __init__(self, elem):
        LinkedList.Record.__init__(self, elem)
        self.prev = None

    def __str__(self):
        return super.__str__()

class ListaDoppiamenteCollegata(LinkedList.ListaCollegata):
    
    def addAsLast(self, elem):
        rec = DoubleRecord(elem)
        if self.first is None:
            self.first = self.last = rec
        else:
            rec.prev = self.last
            self.last.next = rec
            self.last = rec
    
    def addAsFirst(self, elem):
        rec = DoubleRecord(elem)
        if self.first is None:
            self.first = self.last = rec
        else:
            self.first.prev = rec
            rec.next = self.first
            self.first = rec
    
    def popFirst(self):
        if self.first is None:
            return None
        else:
            res = self.first.elem
            self.first = self.first.next
            if self.first is not None:
                self.first.prev = None #Il controllo serve a gestire il caso di lista vuota    
            else:
                self.last = None
            return res

    def popLast(self):
        if self.first is None:
            return None
        else:
            res = self.last.elem
            self.last = self.last.prev
            if self.last is not None:
                self.last.next = None
            else:
                self.first = None
            return res

    def deleteRecord(self, rec):
        if rec is None:
            return
        if rec.prev is not None:
            rec.prev.next = rec.next
        else:
            self.first = rec.next
        if rec.next is not None:
            rec.next.prev = rec.prev
        else:
            self.last = rec.prev

    def __len__(self):
        size = 0
        curr = self.first
        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def __str__(self):
        s = "["
        current = self.first
        while current is not None:
            if len(s) > 1:
                s += ", "
            s += str(current.elem)
            current = current.next
        s += "]"
        return s


if __name__=="__main__":
    l= ListaDoppiamenteCollegata()
    print(l)
    
    print("addAsFirst(2)")
    l.addAsFirst(2)
    print("addAsFirst(3)")
    l.addAsFirst(3)
    print("addAsLast(4)")
    l.addAsLast(4)
    print(l)
    print(len(l))
    
    print("getFirst():", l.getFirst())
    print("getLast():", l.getLast())

    print("popFirst():", l.popFirst())

    print("findFirst():", l.getFirst())
    print("findLast():", l.getLast())

    print("rec1=insertFirst(2)")
    l.addAsFirst(2)
    rec1 = l.getFirstRecord()
    print("rec2=insertFirst(3)")
    l.addAsFirst(3)    
    rec2 = l.getFirstRecord()
    print("rec3=insertLast(4)")
    l.addAsLast(4)
    rec3 = l.getLastRecord()
    print(l)

    print("delete(rec1)")
    l.deleteRecord(rec1)
    print(l)
    print("delete(rec2)")
    l.deleteRecord(rec2)
    print(l)
    print("delete(rec3)")
    l.deleteRecord(rec3)
    print(l)
