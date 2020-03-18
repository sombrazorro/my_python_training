import sys
sys.path.append("..")
from ex14.ex14_dllist import DoubleLinkedList
import ex16_sorting
from random import randint

max_numbers = 30

def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers


def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value:
            return False
        else:
            node = node.next

    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)
    m = numbers.count()
    ex16_sorting.bubble_sort(numbers)
    assert numbers.count() == m
    assert is_sorted(numbers)


def test_merge_sort():
   # numbers = random_list(max_numbers * 31)
    numbers = random_list(max_numbers * 1000)
    m = numbers.count()

    ex16_sorting.merge_sort(numbers)
    assert numbers.count() == m
    assert is_sorted(numbers)

def test_quick_sort_copy():
    numbers = random_list(max_numbers * 31)
    m = numbers.count()
#    print(numbers.dump())
   # ex16_sorting.quick_sort(numbers, 0, numbers.count() - 1)
    r = ex16_sorting.quick_sort_copy(numbers)

#    print(r.dump())
   # assert is_sorted(numbers)
    assert numbers.count() == m
    assert is_sorted(r)



def test_quick_sort():
    numbers = random_list(max_numbers * 1000)
    m = numbers.count()
    print(m)
   # ex16_sorting.quick_sort(numbers, 0, numbers.count() - 1)
    ex16_sorting.quick_sort(numbers)
    assert numbers.count() == m
    assert is_sorted(numbers)
