import sys
sys.path.append("..")
from ex14.ex14_dllist import DoubleLinkedList
from ex20.ex20_binary_searching_tree import BSTree


def bs_list(lt, key):
    result = None
    ll = len(lt)
    # Use "ll" or else since "l" is easily confused with the digit "1".

    if ll > 0:
        mid = lt[ll//2]
    # Handle the empty list
    else:
        return None

    if key == mid:
        # return "Found {}".format(key)
        return mid
    elif ll > 1:
        if key > mid:
            # print(lt[ll//2+1:])
            result = bs_list(lt[ll//2+1:], key)
            # bs_list(lt[l//2+1:], key)
        else:
            # print(lt[0:ll//2])
            result = bs_list(lt[0:ll//2], key)
            # bs_list(lt[l//2+1:], key)
    return result


def bs_list_result(lt, key):
    result = bs_list(lt, key)
    if result:
        idx = lt.index(key)
        return result,idx
    else:
        return result


def bs_dll(dll, key):
    '''Sorted doubly linked list needed for the input argument'''
    result = None
    ll = dll.count()
    tmp = DoubleLinkedList()
    midpt = ll//2  # Note the convention of the midpoint will have an influence
                   # to the following binary division(L53~L65).
    if ll > 0:
        mid = dll.get(midpt)
        i = 0
        midnode = dll.begin
        while i < midpt:
            midnode = midnode.next
            i = i + 1
    else:
        return None

    if key == mid:
        return mid
    elif ll > 1:
        if key > mid:
            while midnode:
                tmp.push(midnode.value)
                midnode = midnode.next
            result = bs_dll(tmp, key)
        else:
            midnode = midnode.prev  # Backforwd once needed firstly since Line 37
                                    # for the conversion of the midpoint index
                                    # Otherwise, infinit function calls occur

            while midnode:
                tmp.shift(midnode.value)
                midnode = midnode.prev
            result = bs_dll(tmp, key)
    return result


def bs_dll_result(lt, key):
    result = bs_dll(lt, key)
    if result:
        midnode = lt.begin
        idx = 0

        # May include this fuction for find indice in ex.14
        while midnode and midnode.value != key:
            midnode = midnode.next
            idx = idx + 1

        return result, idx
    else:
        return result
