class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev


    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return ("[{}, {}, {}]".format(
                 repr(pval), self.value, repr(nval)
                                     )
               )


class Queue(object):


    def __init__(self):
        self.head = None
        self.tail = None


    def _invariant(self):
        if (self.head is None) or (self.tail is None):
            assert self.head == None
            assert self.tail == None
        elif self.head == self.tail:
            assert self.head.next is None
            assert self.tail.prev is None
        else:
            assert self.head.prev is None
            assert self.tail.next == None
        return None

    
    def enqueue(self, obj):
        node = QueueNode(obj, None, None)
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            node.prev = self.tail
            self.tail = node
            self.tail.prev = self.head
            self.head.next = self.tail 
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return None


    def dequeue(self):
        if self.head is None:
            firstvalue = None
        elif self.head == self.tail:
            firstvalue = self.head.value
            self.head = None
            self.tail = None
        else:
            firstvalue = self.head.value
            self.head = self.head.next
            self.head.prev = None
        return firstvalue


    def count(self):
        """Counts the number of elements in the list."""
        x = self.head
        if x is None:
            return 0

        else:
            i = 1
            while True:
                if x.next is not None:
                    i = i + 1
                    x = x.next
                else:
                    break
            return i


    def dump(self, mark=None):
        """Debugging function that dumps the contents of the list."""
        d = []
        x = self.head
      #  c = 0
        if mark is None:
            while x != self.tail:
                d.append(x)
                x = x.next
            d.append(self.tail)
        else:
            pass
            #  while c < mark:
            #      d.append(x)
            #      c = c + 1
            #      x = x.next
        return d
