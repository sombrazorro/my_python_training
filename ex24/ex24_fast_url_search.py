import sys
sys.path.append("..")
from ex14.ex14_dllist import DoubleLinkedList
from ex20.ex20_binary_searching_tree import BSTree
from ex23.ex23_ternary_search_tree import TSTree
from ex17.ex17_dictionary import Dictionary

# This is for the coherence in the test: ex24_fast_url_search_test.py
# Let the nodes of DDList wil have the attribute of "value."
class URLNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class URLRouter(object):
    def __init__(self):
        print('URL establised.')
        # pass

    @classmethod
    def url_string_set(cls, s):
        key_list = ["/"+x+"/" for x in s.strip("/").split("/")]
        return key_list

    def add(self, key, value):
        pass

    def find_exact_match(self, key):
        pass

    def find_part(self, key):
        pass

    def find_best_match(self, key):
        return self.find_part(key)

    def find_all(self, key):
        pass

    def find_shortest(self, key):
        s = sorted([x for x in self.find_all(key)], key=lambda x: len(x.key))
        #print(s)
        return s[0]


    def find_longest(self, key):
        l = sorted([_ for _ in self.find_all(key)], key=lambda _: len(_.key), reverse=True)
        return l[0]


class TSTreeRouter(URLRouter):
    def __init__(self, url=None):
        self.obj = TSTree()
        self.url = url
        if self.url:
            self.obj.set(url, url)
        else:
            pass
       #     keys = super().url_string_set(self.url)
       # for k in keys:
       #    # print(k.strip("/"))
       #     self.obj.set(k, k.strip("/"))

    def add(self, key, value):
        self.obj.set(key, value)

    def find_exact_match(self, key):
        all_results_list = self.obj.find_all(key)
        matched = [x.key == key for x in all_results_list]
        if any(matched):
            return all_results_list[matched.index(True)]
        else:
            return None

    def find_best_match(self, key):
        return self.obj.find_part(key)

    def find_all(self, key):
        return self.obj.find_all(key)

    def find_part(self, key):
        return self.obj.find_part(key)

    def find_shortest(self, key):
        return self.obj.find_shortest(key)

    def find_longest(self, key):
        return self.obj.find_longest(key)


class DLListRouter(URLRouter):
    def __init__(self):
        self.obj = DoubleLinkedList()
    #    super().__init__()
       # self.url = url
    #    if url:
    #        self.obj.push(URLNode(url, url))
    #    else:
    #        pass

    def add(self, key, value):
        self.obj.push(URLNode(key, value))

    def find_exact_match(self, key):
        node = self.obj.begin
        while node:
            if node.value.key == key:
                return node.value # Find only first matched occurance
            else:
               # pass
                node = node.next
        return None

    def find_all(self, key):
        matched_nodes_list = []
        node = self.obj.begin
        while node:
            if key in node.value.key:
                matched_nodes_list.append(node.value)
            else:
                pass
            node = node.next
        return matched_nodes_list

    def find_part(self, key):
        matched_nodes_list = []
        i = 0
        #node = self.obj.begin
        while i < len(key) and matched_nodes_list == []:
            matched_nodes_list = self.find_all(key[:len(key)-i])
            i = i + 1
            print(i, key[:len(key)-i])
        p = sorted([x for x in matched_nodes_list], key=lambda x: len(x.key))
        print([_.key for _ in p])
        return p[0] if p != [] else None

class BSTreeRouter(URLRouter):
    def __init__(self):
        self.obj = BSTree()
        self.result_all = None
        self.result_part = None
#        super().__init__()

    def add(self, key, value):
        self.obj.set(key, URLNode(key, value))
        # chars = [ord(x) for x in key]
        #i = 0
        #for s in chars:
        #    if i < (len(chars) - 1):
        #        self.obj.set(s, None)
        #    elif i == (len(chars) - 1):
        #        self.obj.set(s, URLNode(key, value))
        #    else:
        #        pass
        #    i = i + 1

    def find_exact_match(self, key):
        return self.obj.get(key)

    def find_all(self, key):
        self.result_all = []
#        return self._find_all(key, self.obj.root)

        def _find_all_test(key, node):
            if node:
                if len(node.key) >= len(key):
                    if node.key.startswith(key):
                        self.result_all.append(node.value)
                else:
                    pass
                _find_all_test(key, node.left)
                _find_all_test(key, node.right)
            return self.result_all

        return _find_all_test(key, self.obj.root)

#    def _find_all(self, key, node):
#        if node:
#            if len(node.key) >= len(key):
#                if node.key.startswith(key):
#                    self.result_all.append(node.value)
#            else:
#                pass
#
#            self._find_all(key, node.left)
#            self._find_all(key, node.right)
#        return self.result_all
    def find_part(self, key):
        #result_part = []

        def _find_part_test(key, node, result):
            #result = []
            if node:
                if len(node.key) >= len(key):
                    if node.key.startswith(key):
                        result.append(node.value)
                else:
                    pass
                _find_part_test(key, node.left, result)
                _find_part_test(key, node.right, result)
               # result = min([result, result_left, result_right], key=lambda x: len(x.key))
            return result

        result_part = None
        for i in range(1, len(key)+1):
            tmp_result_part = _find_part_test(key[:i], self.obj.root, [])
            print(i, [x.key for x in tmp_result_part])
            if not tmp_result_part:
                break
            else:
                pass
            result_part = tmp_result_part

        #sorted_result = sorted(list(set([x for x in self.result_part])), key = lambda x: x.key)
        if result_part:
            result_part = sorted([x for x in result_part], key = lambda x: x.key)
        else:
            pass

        #for _ in sorted_result:
        #    print(_.key)
        return result_part[0] if result_part else result_part


class pyDictRouter(URLRouter):
    def __init__(self):
        self.obj = {}

    def add(self, key, value):
        self.obj[key] = URLNode(key, value)

    def find_exact_match(self, key):
        if key in self.obj:
            return self.obj[key]

    def find_all(self, key):
        return [self.obj[x] for x in self.obj.keys() if x.startswith(key)]

    def find_part(self, key):
        def _find_part(key, result):
            for k in self.obj.keys():
                if len(k) >= len(key) and k.startswith(key):
                    print(k)
                    result.append(self.obj[k])
                else:
                    pass
            return result
        matched_nodes_list = []
        for i in range(1, len(key)+1):
            tmp_result_part = _find_part(key[:i], [])
            print("tmp_result_part", (key[:i],[x.value for x in tmp_result_part]))
            
            if tmp_result_part == []:
                break
            else:
                matched_nodes_list = tmp_result_part
            
        p = sorted([x for x in matched_nodes_list], key=lambda x: len(x.key))
        print([_.key for _ in p])
        return p[0] if p != [] else None


class DictRouter(URLRouter):
    def __init__(self):
        self.obj = Dictionary()

    def add(self, key, value):
        self.obj.set(key, URLNode(key, value))


    def find_exact_match(self, key):
        return self.obj.get(key)

    def find_all(self, key):
        return [self.obj.get(x) for x in self.obj.get_keys() if x.startswith(key)]

    def find_part(self, key):
        def _find_part(key, result):
            for k in self.obj.get_keys():
                if len(k) >= len(key) and k.startswith(key):
                    print(k)
                    result.append(self.obj.get(k))
                else:
                    pass
            return result
        matched_nodes_list = []
        for i in range(1, len(key)+1):
            tmp_result_part = _find_part(key[:i], [])
            print("tmp_result_part", (key[:i], [x.value for x in tmp_result_part]))
            
            if tmp_result_part == []:
                break
            else:
                matched_nodes_list = tmp_result_part
            
        p = sorted([x for x in matched_nodes_list], key=lambda x: len(x.key))
        print([_.key for _ in p])
        return p[0] if p != [] else None

