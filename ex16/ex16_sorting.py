import sys
sys.path.append("..")
from ex14.ex14_dllist import *


# p-code for Bubble sort from wiki
# procedure bubbleSort( A : list of sortable items )
#     n = length(A)
#     repeat
#         swapped = false
#         for i = 1 to n-1 inclusive do
#             /* if this pair is out of order */
#             if A[i-1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap( A[i-1], A[i] )
#                 swapped = true
#             end if
#         end for
#     until not swapped
# end procedure

# procedure bubbleSort( A : list of sortable items )
def bubble_sort(dll):
    while True:
        swapped = False
        node = dll.begin
        while node != dll.end:
            if (node.value > node.next.value):
                v = node.value
                node.value = node.next.value
                node.next.value = v
                swapped = True
            node = node.next
        if not swapped:
            break
    return dll.dump()



# p-codes from wiki for top-down merge_sort
# ===================================
# function merge_sort(list m)
#     // Base case. A list of zero or one elements is sorted, by definition.
#     if length of m ≤ 1 then
#         return m
#
#     // Recursive case. First, divide the list into equal-sized sublists
#     // consisting of the first half and second half of the list.
#     // This assumes lists start at index 0.
#     var left := empty list
#     var right := empty list
#     for each x with index i in m do
#         if i < (length of m)/2 then
#             add x to left
#         else
#             add x to right
#
#     // Recursively sort both sublists.
#     left := merge_sort(left)
#     right := merge_sort(right)
#
#     // Then merge the now-sorted sublists.
#     return merge(left, right)
#
# function merge(left, right)
#     var result := empty list
#
#     while left is not empty and right is not empty do
#         if first(left) ≤ first(right) then
#             append first(left) to result
#             left := rest(left)
#         else
#             append first(right) to result
#             right := rest(right)
#
#     // Either left or right may have elements left; consume them.
#     // (Only one of the following loops will actually be entered.)
#     while left is not empty do
#         append first(left) to result
#         left := rest(left)
#     while right is not empty do
#         append first(right) to result
#         right := rest(right)
#     return result
# ============================================

# function merge_sort(list m)
#     // Base case. A list of zero or one elements is sorted, by definition.
#     if length of m ≤ 1 then
#         return m
#def merge_sort(dll):
#    m = dll.count()
#    if m > 1:
#        left = DoubleLinkedList()
#        right = DoubleLinkedList()
#        c = 0
#        while dll.begin:
#            if c < m/2:
#                left.push(dll.begin.value)
#                dll.begin = dll.begin.next
#                c = c + 1
#            else:
#                right.push(dll.begin.value)
#                dll.begin = dll.begin.next
#                c = c + 1
#
#        assert c == m
#        print(("left", left.dump()))
#        print(("right", right.dump()))
#        left = merge_sort(left)
#        right = merge_sort(right)
#        return merge(left, right)
#    else:
#        return dll
#
#
#def merge(left, right):
#    result = DoubleLinkedList()
#    while left.begin and right.begin:
#        if left.begin.value <= right.begin.value:
#            result.push(left.begin.value)
#            left.begin = left.begin.next
#        else:
#            result.push(right.begin.value)
#            right.begin = right.begin.next
#
#    while left.begin:
#        result.push(left.begin.value)
#        left.begin = left.begin.next
#    while right.begin:
#        result.push(right.begin.value)
#        right.begin = right.begin.next
#    return result


def merge_sort(dll):
    s = seperate(dll)
    dll.begin = s.begin
    dll.end = s.end
    return None

def merge_sort_1(dll):
    dll = seperate(dll)
    return dll


def seperate(dll):
    m = dll.count()

    if m > 1:
        left = DoubleLinkedList()
        right = DoubleLinkedList()
        c = 0
        while dll.begin:
            if c < m/2:
                left.push(dll.begin.value)
                dll.begin = dll.begin.next
                c = c + 1
            else:
                right.push(dll.begin.value)
                dll.begin = dll.begin.next
                c = c + 1

        assert c == m
       # print(("left", left.dump()))
       # print(("right", right.dump()))
        left = seperate(left)
        right = seperate(right)
        s = merge(left, right)
        return s
    else:
        return dll


def merge(left, right):
    result = DoubleLinkedList()
    while left.begin and right.begin:
        if left.begin.value <= right.begin.value:
            result.push(left.begin.value)
            left.begin = left.begin.next
        else:
            result.push(right.begin.value)
            right.begin = right.begin.next
    while left.begin:
        result.push(left.begin.value)
        left.begin = left.begin.next
    while right.begin:
        result.push(right.begin.value)
        right.begin = right.begin.next
    return result


def quick_sort_copy(dll):
    m = dll.count()
    if m > 1:
        x = dll.last()
        node = dll.begin
        small = DoubleLinkedList()
        large = DoubleLinkedList()
        while node != dll.end:
            if node.value <= x:
                small.push(node.value)
            #    node = node.next
            else:
                large.push(node.value)
            node = node.next

        if large.begin is None:
            small = quick_sort_copy(small)
            small.push(x)
            return small
        else:
        #    print(small.dump())
        #    print(large.dump())
            small = quick_sort_copy(small)
            large = quick_sort_copy(large)
      #      small._invariant()
      #      large._invariant()
         #   print(small.dump())
         #   print(large.dump())
            small.push(x)
            #print(small.dump())
            small.end.next = large.begin
            large.begin.prev = small.end
 #           print(small.dump())
            small.end = large.end
            return small
    else:
#        print(dll.dump())
#        assert dll._invariant() is None
        return dll


def quick_sort(dll):
    m = dll.count()
    if m > 1:
        x = dll.last()
#        dll.begin = dll.begin
        small = DoubleLinkedList()
        large = DoubleLinkedList()
        while dll.begin != dll.end:
            if dll.begin.value <= x:
                small.push(dll.begin.value)
            #    dll.begin = dll.begin.next
            else:
                large.push(dll.begin.value)
            dll.begin = dll.begin.next
      #  print(small.dump())
        small = quick_sort(small)
      #  print(small.dump())
  #      print(large.dump())
        large = quick_sort(large)
  #      print(large.dump())
        merged = merge_q(small, x, large)
        dll.begin = merged.begin  # Is this good? Does this consume memory much?
        dll.end = merged.end
        return merged
    else:
        return dll


def merge_q(small, midnode, large):
    result = DoubleLinkedList()
    if small.begin is None and  large.begin is None:
        result.push(midnode)
 #       print(("1", result.dump()))
        print("Something odd!")
        return result
    elif small.begin is None:
        large.shift(midnode)
        result = large
 #       print(("2", result.dump()))
        return result
    elif large.begin is None:
        small.push(midnode)
        result = small
  #      print(("3", result.dump()))
        return result
    else:
        small.push(midnode)
        result = small
        result.end.next = large.begin
        result.end.next.prev = result.end
        result.end = large.end
  #      print(("4", result.dump()))
        return result
