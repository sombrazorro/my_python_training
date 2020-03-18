from ex15_stack import *


def test_push():
    stk = Stack()
    stk.push(1)
   # stk.# _invariant()
    assert stk.count() == 1
    stk.push(2)
   # stk.# _invariant()
    assert stk.count() == 2
    return None

def test_pop():
    stk = Stack()
    stk.push(1)
    stk.pop()
  #  stk._invatiant()
    stk.push(1)
    stk.push(2)
    stk.push(3)
  #  stk.# _invariant()
    stk.pop() == 3
 #   stk.# _invarinat()
    stk.pop() == 2
    stk.pop() == 1
    stk.pop() == None
  #  stk.# _invarinat()
    return None

def test_top():
    stk = Stack()
    stk.push(1)
    stk.top() == 1
  #  stk.# _invariant()
    stk.push(2)
    stk.top() == 2
    stk.push(3)
    stk.top() == 3
    stk.pop()
    stk.top() == 2
    stk.pop()
    stk.top() == 1
    stk.pop()
    stk.top() == None
    return None
