import sys
import argparse
sys.path.append("..")
from ex14.ex14_dllist import DoubleLinkedList
import ex19_sort_performance_improvement
from random import randint

parser = argparse.ArgumentParser(prog='ex19_sort_performance_improvement_test.py')
parser.add_argument('-n', metavar="length", type=int, help='list length for sorting')

parser.add_argument('-l', metavar="loops", type=int, help='number of iteration')

args = parser.parse_args()
if args.l and args.l > 2:
    l= args.l
else:
    l = 2

#print("Numbers of iteration:" + str(l-1))
#var = input("Please enter the max_number from 1 to 1000 (default=100): ")
var=args.n
#if var.isdigit() and int(var) in range(1,1001):
if var in range(1,1001):
#    print("You entered " + str(var))
    max_numbers = int(var)
else:
    print("Just use the default(=100) length for sorting!")
    max_numbers = 100

print("length " + str(max_numbers) + "in " + "Numbers of iteration:" + str(l-1) )    

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
    ex19_sort_performance_improvement.bubble_sort(numbers)
    assert numbers.count() == m
    assert is_sorted(numbers)


def test_merge_sort():
    numbers = random_list(max_numbers)
   # numbers = random_list(max_numbers * 1000)
    m = numbers.count()

    ex19_sort_performance_improvement.merge_sort(numbers)
    assert numbers.count() == m
    assert is_sorted(numbers)

    
def test_quick_sort_copy():
    numbers = random_list(max_numbers)
    m = numbers.count()
#    print(numbers.dump())
   # ex19_sort_performance_improvement.quick_sort(numbers, 0, numbers.count() - 1)
    r = ex19_sort_performance_improvement.quick_sort_copy(numbers)

#    print(r.dump())
   # assert is_sorted(numbers)
    assert numbers.count() == m
    assert is_sorted(r)


def test_quick_sort():
    numbers = random_list(max_numbers)
   # numbers = random_list(max_numbers * 1000)
    m = numbers.count()
    print(m)
   # ex19_sort_performance_improvement.quick_sort(numbers, 0, numbers.count() - 1)
    ex19_sort_performance_improvement.quick_sort(numbers)
    assert numbers.count() == m
    assert is_sorted(numbers)


# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("test_bubble_sort()", setup="from __main__ import test_bubble_sort", number=10000))


if __name__ == '__main__':
    for i in range(1,l):
        test_bubble_sort()
        test_merge_sort()
        test_quick_sort()
        test_quick_sort_copy()
