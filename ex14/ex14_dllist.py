class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
      #  if self.next and self.next.value == 0:
      #      nval = 0  # Since "0 or None" will show None.
      #  else:
      #      nval = self.next and self.next.value or None
      #  if self.prev and self.prev.value == 0:
      #      pval = 0  # The same reason as Line 10.
      #  else:
      #      pval = self.prev and self.prev.value or None
        nval = self.next.value if self.next else None
        pval = self.prev.value if self.prev else None
        # return f"[{self.value}, {repr(nval)}, {repr(pval)}]"
        return ("[{}, {}, {}]".format(
                  repr(pval), self.value, repr(nval)
               ))


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def _invariant(self):
        if (self.begin is None) or (self.end is None):
            print("Case 1 checking...")
            assert self.begin is None
            assert self.end is None
            print("ok")

        elif self.begin == self.end:
            print("Case 2 checking...")
            assert self.begin.next is None
            assert self.end.prev is None
            print("ok")

        else:
            print("Case 3 checking...")
            assert self.begin.prev is None
            assert self.end.next is None
            print("ok")

        return None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = DoubleLinkedListNode(obj, None, None)
        if (self.begin is None) and (self.begin is None):
            self.begin = node
            self.end = self.begin
        elif self.begin == self.end:
            node.prev = self.end
            self.end = node
            self.end.prev = self.begin
            self.begin.next = self.end
#            print(self.begin)
#            print(self.end)
        else:
            node.prev = self.end
            self.end.next = node
            self.end = node

        return None

    def pop(self):
        """Removes the last item and returns it."""
        if self.end is None:
            lastvalue = None
        elif self.begin == self.end:
            lastvalue = self.end.value
            self.begin = None
            self.end = None
        else:
            lastvalue = self.end.value
            # midnode = self.end.prev
            self.end = self.end.prev
            self.end.next = None
        return lastvalue

    def shift(self, obj):
        """Push obj from the other side."""
        node = DoubleLinkedListNode(obj, None, None)
        if self.begin is None:
            self.begin = node
            self.end = node
        elif self.begin == self.end:
            node.next = self.begin
            self.begin = node
            self.begin.next = self.end
            self.end.prev = self.begin
#            print(self.begin)
#            print(self.end)
        else:
            node.next = self.begin
            self.begin.prev = node
            self.begin = node
        return None

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        # midnode = self.begin
        if self.begin is None:
            firstvalue = None
        elif self.begin == self.end:
            firstvalue = self.end.value
            self.begin = None
            self.end = None
        else:
            firstvalue = self.begin.value
            self.begin = self.begin.next
            self.begin.prev = None
        return firstvalue

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove().  It should take a node, and detach it from
        the list, whether the node is at the front, end, or in the middle."""
        if node.prev is None and node.next is None:
            self.begin is None   # Handle the some instance variables directly,
            self.end is None     # like self.begin. One also can use member method,
        elif node.prev is None:  # self.shift or self.pop to achieve the detaching.
            node = node.next
            node.prev = None
            self.begin = node

        elif node.next is None:
            node = node.prev
            node.next = None
            self.end = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return None
 #   def idx(self, obj):
 #       i = 0
 #       while node:
 #           if node.value == obj:
 #               break
 #           node = node.next
 #           i = i + 1
 #       return i


    def remove(self, obj):
        node = self.begin
        i = 0
        while node:
            if node.value == obj:
                self.detach_node(node)
                break
            node = node.next
            i = i + 1
        return i

    def remove_old(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        i = 0
        if self.begin is None:
            i = None
        elif self.begin == self.end:
            if self.begin.value == obj:
                self.begin = None
                self.end = None
            else:
                i = None
                pass
        elif self.begin.value == obj:
            self.begin = self.begin.next
            self.begin.prev = None

        else:
            while node:
                if node.value == obj:
                    if node != self.end:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        node = node.next
                    #    i = i + 1
                    else:
                         self.end = node.prev
                         self.end.next = None
                    break
                else:

                    if (node.next == self.end and node.next.value != obj):
                        i = None     # If the obj does not show up the linked list,
                        break        # the linked list should not be altered and return None.
                    node = node.next
                    i = i + 1
        return i

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
       # if not self.begin:
       #    firstvalue = None
       # else:
       #    firstvalue = self.begin.value
       # return firstvalue
        return self.begin and self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end and self.end.value

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
        # c = 0
        if x and mark is None:
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
