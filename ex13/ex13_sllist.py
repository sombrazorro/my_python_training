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
        """Appends a new value on the end of the list."""
        self.begin = SingleLinkedListNode(obj, self.begin)
        return None

    def pop(self):
        """Removes the last item and returns it."""
        if self.begin is not None:
            last_val = self.begin.value
            self.begin = self.begin.next
            return last_val
        else:
            return None

    def shift(self, obj):
        """Another name for push."""
        st = SingleLinkedList(obj, None)
        self.end = SingleLinkedListNode(obj, self.end)
        self.begin = SingleLinkedListNode(obj, self.begin.next)
        #self.end = self.begin
      # if self.begin is None:
      #      previous = None
      #  else:
      #      previous = self.begin.value
      #  self.end = SingleLinkedListNode(obj, self.end)
      #  self.begin = SingleLinkedListNode(previous, self.begin)
        # begin_val = self.begin.value
        return None



    def unshift(self):
        """Removes the first item and returns it."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove."""

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

    def dump(self, mark=None):
        """Debugging function that dumps the contents of the list."""
        d = []
        x = self.begin
        c = 0
        if mark is None:
            while x is not None:
                if mark is None:
                    d.append(x)
                    x = x.next
                else:
                    while c < mark:
                        d.append(x)
                        c = c + 1
                        x = x.next
        return d
