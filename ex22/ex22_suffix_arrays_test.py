import sys
sys.path.append("..")
import random
import string
#from ex14.ex14_dllist import DoubleLinkedList
from ex22_suffix_arrays import find_shortest
from ex22_suffix_arrays import find_longest
from ex22_suffix_arrays import find_all
from ex22_suffix_tree import suffix_tree


magic = "abracadabra"
addendum = "aaaabababc"


def test_find_shortest():
    assert find_shortest(magic, "a") == "a"
    assert find_shortest(magic, magic) == magic
    assert find_shortest(magic, "abra") == "abra"
    assert find_shortest(magic, "ra") == "ra"
    assert find_shortest(magic + addendum, "a") == "abc"
    return None


def test_find_longest():
    assert find_longest(magic, "abra") == magic
    assert find_longest(magic, "ra") == "racadabra"
    assert find_longest(magic, "d") == "dabra"
    return None


def test_find_all():
    print(find_all(magic, magic))
    assert find_all(magic, magic) == (magic,)
    print(find_all(magic, "abra"))
    assert find_all(magic, "abra") == ("abra", magic)
    print(find_all(magic, "a"))

    rslt = tuple(sorted(["a", "abra", "adabra", "acadabra", magic]))
    assert find_all(magic, "a") == rslt
    print(find_all(magic, "ada"))
    assert find_all(magic + addendum, "ada") == ("adabra" + addendum,)
    return None


def test_stf_find_shortest():
    s = suffix_tree(magic)
    assert s.sft_find_shortest("a") == "a"
    assert s.sft_find_shortest(magic) == magic
    assert s.sft_find_shortest("abra") == "abra"
    assert s.sft_find_shortest("ra") == "ra"
    t = suffix_tree(magic+addendum)
    assert t.sft_find_shortest("a") == "abc"
    return None


def test_stf_find_longest():
    s = suffix_tree(magic)
    assert s.sft_find_longest("abra") == magic
    assert s.sft_find_longest("ra") == "racadabra"
    assert s.sft_find_longest("d") == "dabra"
    return None


def test_stf_find_all():
    s = suffix_tree(magic)
    print(s.sft_find_all(magic))
    assert s.sft_find_all(magic) == (magic,)
    print(s.sft_find_all("abra"))
    assert s.sft_find_all("abra") == ("abra", magic)
    print(s.sft_find_all("a"))

    rslt = tuple(sorted(["a", "abra", "adabra", "acadabra", magic]))
    assert s.sft_find_all("a") == rslt
    print(s.sft_find_all("ada"))
    t = suffix_tree(magic+addendum)
    assert t.sft_find_all("ada") == ("adabra" + addendum,)
    return None


def test_random_stf_list():
    for _ in range(200):
        n = random.randint(0,14)
        m = random.randint(0,n)
        s = "".join((random.choice(string.ascii_lowercase) for _ in range(n)))
        pat = s[:2] # "".join((range))
        #pat = "".join((random.choice(string.ascii_lowercase) for _ in range(m)))
       # print(suffix_tree(s).sft_find_shortest_1(pat))
       # print(find_shortest(s, pat))

        if suffix_tree(s).sft_find_shortest_1(pat) != find_shortest(s, pat):
            print("Find_shortest: ({}, {})".format(s, pat))
        else:
            pass
        if suffix_tree(s).sft_find_longest(pat) != find_longest(s, pat):
            print("Find_longest: ({}, {})".format(s, pat))
        else:
            pass
      #  if suffix_tree(s).sft_find_all(pat) != find_all(s, pat):
      #     print("Find_all: ({}, {})".format(s, pat))
      # else:
      #     pass
