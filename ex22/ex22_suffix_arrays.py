import sys
sys.path.append("..")
from ex14.ex14_dllist import DoubleLinkedList


#magic = "abracadabra"
#magic_sa = sorted([magic[i:] for i in range(0, len(magic))])
#print(magic_sa)


def find_shortest(words,  pat):
    ws = sorted([words[i:] for i in range(0, len(words))])
    result = [x for x in ws if pat == x[:len(pat)]]
    return sorted(result, key=len)[0] if result != [] else None


def find_longest(words,  pat):
    ws = sorted([words[i:] for i in range(0, len(words))], reverse=True)
    result = [x for x in ws if pat == x[:len(pat)]]
    return sorted(result, reverse=True, key=len)[0] if result != [] else None


def find_all(words,  pat):
    ws = sorted([words[i:] for i in range(0, len(words))])
    return tuple([x for x in ws if pat == x[:len(pat)]])
