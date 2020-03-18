sys.path.append("..")
from ex14.ex14_dllist import DoubleLinkedList
from ex21_binary_search import bs_list_result
from ex21_binary_search import bs_dll_result


data = sorted([5,3,7,1,9,20])
def test_bs_list_result():
    assert bs_list_result(data, 5) == (5, 2)
    assert bs_list_result(data, 1) == (1, 0)
    assert bs_list_result(data, 20) == (20, len(data) - 1)
    assert bs_list_result(data, 9) == (9, 4)
    assert bs_list_result(data, 100) is None
    assert bs_list_result(data, -1) is None


def test_bs_dll_result():
    data_n = DoubleLinkedList()
    for i in data:
        data_n.push(i)
    #print(data)
    #print(data_n.dump())
    assert bs_dll_result(data_n, 5) == (5, 2)
    assert bs_dll_result(data_n, 1) == (1, 0)
    assert bs_dll_result(data_n, 20) == (20, len(data) - 1)
    assert bs_dll_result(data_n, 9) == (9, 4)
    assert bs_dll_result(data_n, 100) is None
    assert bs_dll_result(data_n, -1) is None
