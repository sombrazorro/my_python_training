class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
#        return f"[{self.value}:{repr(nval)}]"
        return "[{}:{}]".format(self.value, nval)


# Singly linked list to list
def tolist(x):
    r = []
    while True:
        if x is not None:
            r.append(x.value)
            x = x.next
        else:
            break
    return r

# Version 1:
# def tosll(x):
#     i = 0
#     d = {}
#     x.reverse()
#     d[i] = SingleLinkedListNode(None, None)
#     while i < len(x):
#         i = i + 1
#         d[i] = SingleLinkedListNode(x[i-1], d[i-1])
#     return d


def toSll(x):
    i = 0
    x.reverse()
    d = SingleLinkedListNode(None, None)
    while i < len(x):
        i = i + 1
        d = SingleLinkedListNode(x[i-1], d)
    return d


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.end = node
            self.end.next = None
            self.begin = self.end
        else:
            self.end.next = node
            self.end = node
            self.end.next = None
        return None
#    def push(self, obj):
#        """Appends a new value on the end of the list."""
#        self.begin = SingleLinkedListNode(obj, self.begin)
#        return None

    def pop(self):
        """Removes the last item and returns it."""
        midnode = self.begin
        if self.begin is None:
            assert self.end is None
            lastvalue = None
        elif self.begin != self.end:
            while midnode.next != self.end:
                print(midnode)

                midnode = midnode.next
            lastvalue = self.end.value
            #print(midnode)
            self.end = midnode
            self.end.next = None
        else:
            lastvalue = self.end.value
            self.begin = None
            self.end = None
        return lastvalue

    
    def pop1(self):
       """Removes the last item and returns it."""
       if self.end == None:
           return None
       elif self.end == self.begin:
           node = self.begin
           self.end = self.begin = None
           return node.value
       else:
           node = self.begin
           while node.next != self.end:
               node = node.next
           assert self.end != node
           self.end = node
           return node.next.value


    def shift(self, obj):
        """Another name for push."""
        #self.end = SingleLinkedListNode(obj, self.end)
        node = SingleLinkedListNode(obj, None)
        if self.end is None:
           # self.begin = SingleLinkedListNode(None, node)
            self.begin = node
            self.begin.next = None
            assert self.begin != None

            self.end = self.begin
            assert self.end != None

            print("Cd1. begin:{}, end:{}".format(id(self.begin), id(self.end)))
        else:
            self.begin = SingleLinkedListNode(obj, self.begin)
            print("Cd2. begin:{}, end:{}".format(id(self.begin), id(self.end)))
            assert self.begin != None
            assert self.end != self.begin

        return None


    def unshift(self):
        """Removes the first item and returns it."""
        midnode = self.begin
        if self.begin is None:
            firstvalue = None
            assert self.end == self.begin
            
        elif self.begin != self.end:
            #while midnode.next != self.end:
            #    print(midnode)
            firstvalue = self.begin.value
            midnode = midnode.next
            self.begin = midnode
           # self.end.next = None
        else:
            assert self.end != None

            firstvalue = self.end.value
            self.begin = None
            self.end = None
        return firstvalue


    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        i = 0
        if self.begin is None:
            assert self.end == self.begin
            i = None
        elif self.begin == self.end:
            self.begin = None
            self.begin = None
        elif self.begin.value == obj:
            self.begin = self.begin.next
        else:
         #   if node.next.next != self.end:
            while node != self.end:
                if node.next.value == obj:
                    if node.next != self.end:
                        node.next = node.next.next
                        node = node.next
                        i = i + 1
                    else:
                        i = i + 1         # Nodes arrive the last two position \
                                          # and finds 'obj' occurring at the last.
                        node.next = None  # Finalizing the linked list immediately.
                        break             # Add one to 'i' since the finalization never
                                          # perform node.next.
                else:
                    node = node.next
                    i = i + 1
            self.end = node
        return i


    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if not self.first:
            firstvalue = None
        else:
            firstvalue = self.begin.value

        return firstvalue


    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value


    def count(self):
        """Counts the number of elements in the list."""
        x = self.begin
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


    def get(self, index):
        """Get the value at index."""
        i = 0
        midnode = self.begin
        if not self.end:
            v = None
        else:
            v = midnode.value
            while i != index:
                midnode = midnode.next
                if midnode:
                    v = midnode.value
                    i = i + 1
                else:
                    v = None
                    break
        return v

    
    def dump(self, mark=None):
        """Debugging function that dumps the contents of the list."""
        d = []
        x = self.begin
      #  c = 0
        if mark is None:
            while x != self.end:
                d.append(x)
                x = x.next
            d.append(self.end)
        else:
            pass
            #  while c < mark:
            #      d.append(x)
            #      c = c + 1
            #      x = x.next
        return d



print("Testing...")
print(test_push())
print(test_pop())
print(test_unshift())
print(test_shift())
print(test_remove())
print(test_first())
print(test_last())
print(test_get())
print("Tests end.")
# print(test_())    

    
