from ex15_queue import *


def test_enqueue():
    lines = Queue()
    lines._invariant()
    assert lines.count() == 0
    lines.enqueue(1)
    lines._invariant()
    assert lines.head.value == 1
    assert lines.tail.value == 1
    assert lines.count() == 1
    lines.enqueue(2)
    lines._invariant()
    assert lines.head.value == 1
    assert lines.tail.value == 2
    assert lines.count() == 2
    return None


def test_dequeue():
    lines = Queue()
    lines._invariant()
    assert lines.dequeue() == None
    lines.enqueue(1)
    lines.enqueue(2)
    lines.enqueue(3)
    lines._invariant()
    assert lines.count() == 3
    assert lines.head.value == 1
    assert lines.tail.value == 3
    assert lines.dequeue() == 1
    assert lines.count() == 2
    assert lines.head.value == 2
    assert lines.tail.value == 3
    assert lines.dequeue() == 2
    assert lines.count() == 1
    assert lines.head.value == 3
    assert lines.tail.value == 3
    assert lines.dequeue() == 3
    assert lines.count() == 0
    lines._invariant()
 #   assert lines.head == None
 #   assert lines.tail == None
    assert lines.dequeue() == None
    lines._invariant()
 #   assert lines.head == None
 #   assert lines.tail == None
    assert lines.count() == 0
    return None
