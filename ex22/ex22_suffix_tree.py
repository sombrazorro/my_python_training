import sys
sys.path.append("..")
from ex20.ex20_binary_searching_tree import BSTree


class suffix_tree(object):
    def __init__(self, words):
        self.words = words
        self.tree = BSTree()
        self._find_all_rslt = None
        for i in range(0, len(self.words)):
            key = words[i:]
            self.tree.set(key, i)

    def sft_find_shortest(self, sub):
        midnode = self.tree.root
        rlt = None

        while midnode and sub == midnode.key[:len(sub)]:
            rlt = midnode.key
            assert midnode.key != ""  # prevent the empty since not 0 is True

            right = (midnode.right and
                     sub == midnode.right.key[:len(sub)] and
                     len(midnode.right.key)
                     )
            left = (midnode.left and
                    sub == midnode.left.key[:len(sub)] and
                    len(midnode.left.key)
                    )

            if not left and not right: # "if left is None and right is None:..."
                                     # This expression can not filtered the case
                                     # of False.
                break
            elif left and right:
                assert len(midnode.left.key) != len(midnode.right.key)
                if left > right:
                    midnode = midnode.right
                elif left < right:
                    midnode = midnode.left

            elif left:
                midnode = midnode.left
            elif right:
                midnode = midnode.right
            else:
                print("Odd:")
                print((midnode.right.key, midnode.key, midnode.left.key))
                print(("right:{}".format(right)))
                print(("left:{}".format(left)))

                print("break!")
                break
        return rlt

    def sft_find_shortest_1(self, sub):
        midnode = self.tree.root  # "self.tree.root"
                                  # is invalid expression.
        rlt = None
        while midnode and midnode.key and sub in midnode.key:
            if sub == midnode.key[:len(sub)]:
                rlt = midnode.key   # I don't prefer use "return
                # midnode".
            else:
                pass

            if sub > midnode.key:
                midnode = midnode.right
            elif sub < midnode.key:
                midnode = midnode.left
            elif sub == midnode.key:
                break
            else:
                print("Odd!")
                print((midnode.right and midnode.right.key, midnode.key, midnode.left and midnode.left.key))
                print("break!")
                break
        return rlt

    def sft_find_longest(self, sub):
        midnode = self.tree.root  # "self.tree.root"
                                  # is invalid expression.
        rlt = None
        while midnode and midnode.key and sub != "":
            if sub == midnode.key[:len(sub)]:
                rlt = midnode.key  # I don't prefer use "return
                break              # midnod".
            else:
                if sub > midnode.key:
                    midnode = midnode.right
                elif sub < midnode.key:
                    midnode = midnode.left
                else:
                    print("Odd!")
                    break
        return rlt

    def _sft_find_all_1(self, node, sub):
        if node and (sub == node.key[:len(sub)]):
            self._sft_find_all_1(node.left, sub)
            print(node.key)
            self._sft_find_all_1(node.right, sub)

    def _sft_find_all(self, node, sub):
        if node.key:
            self._sft_find_all(node.left, sub)
            if sub == node.key[:len(sub)]:
                self._find_all_rslt.append(node.key)
            self._sft_find_all(node.right, sub)

    def sft_find_all(self, sub):
        self._find_all_rslt = []
        self._sft_find_all(self.tree.root, sub)
        return tuple(self._find_all_rslt)
