class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
       # return f"[{self.value}:{repr(nval)}]"
        return "[{}:{}]".format(self.value, nval)


class Stack(object):

    def __init__(self):
        self.begin = None


    #def _invarient(self):

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        self.begin = StackNode(obj, self.begin)
        return None


    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        # show current value.
        v = self.begin and self.begin.value or None
        # Then, detach the current node.
        # If nodes go to a next term before to next to last term
      #  if self.begin and self.begin.next:
      #      self.begin = self.begin.next
      #  # Else, self.begin = None
      #  else:
      #      self.begin = None
        if (not self.begin) or (not self.begin.next):  # If not self.begin == True, then the
            self.begin = None                         # last condition will not be checked.
        else:
            self.begin = self.begin.next

        return v


    def top(self):
        """Returns a *reference* to the first item, does not remove."""
        # Show the current value.
        v = self.begin and self.begin.value
        return v

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        # Show the current value.
        v = self.begin.value
        return v

    def count(self):
        """Counts the number of elements in the stack."""
        # Expanding self.begin recursivly to None
        i = 0
        x = self.begin
        while x:
            x = x.next
            i = i + 1
        return i


    # def dump(self, mark="----"):
    def dump(self, mark=None):
        """Debugging function that dumps the contents of the stack."""
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
