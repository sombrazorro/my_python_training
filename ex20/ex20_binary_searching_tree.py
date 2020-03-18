class BSTreeNode(object):
    def __init__(self, key=None, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return ("({p},({l},{k},{r}))".format(
                 p=self.parent and self.parent.key, l=self.left,
                 k=self.key, r=self.right
                 ))


class BSTree():
    def __init__(self):
        self.root = BSTreeNode()
        self.list_print = None

    def find_node(self, key):
        midnode = self.root
        # Note the case of empty tree
        while (midnode and midnode.key and (midnode.key != key)):
            if key < midnode.key:
                # print(midnode)
                midnode = midnode.left
            elif key > midnode.key:
                midnode = midnode.right
            # Comment the else statement and use midnode != key
            # for the compactnese.
            # else:
            #     break
        return midnode

    def get(self, key):
        finded = self.find_node(key)
        return finded and finded.key and finded.value

    def set(self, key, value):
        midnode = self.root
        if not self.root.key:
            self.root.key = key
            self.root.value = value
        else:
            midnode = self.root
            while (midnode and midnode.key):
                if key < midnode.key:
                    lastnode = midnode
                    midnode = midnode.left
                elif key > midnode.key:
                    lastnode = midnode
                    midnode = midnode.right
                else:
                    midnode.value = value
                    break
            # After while loop , midnode will be None or not.
            if midnode:
                pass

            # Construct nodes for left or right for its
            # parent in the following.
            elif not midnode:
                midnode = BSTreeNode(key, value)
                midnode.parent = lastnode
                # print("lastnode key:{}".format(lastnode.key))
                if key < lastnode.key:
                    lastnode.left = midnode
                elif key > lastnode.key:
                    lastnode.right = midnode
                else:
                    print("Odd 1 here.")
        return midnode.key and midnode.value

    def walk_in_order(self, node):
        if node:
            self.walk_in_order(node.left)
            self.list_print.append((node.key))
            print(node.key)
            self.walk_in_order(node.right)
        return None

    def list(self):
        self.list_print = []
        self.walk_in_order(self.root)
        return None

    def min(self, node):
        while node.left:
            node = node.left
        return node

    def max(self, node):
        while node.right:
            node = node.right
        return node

    def successor(self, node):
        # right-most subtree is not empty
        if node.right:
            return self.min(node.right)

        # Finds the lowest ancestor if the right-most
        # subtree is empty.
        while (node.parent and node.parent.right == node):
            node = node.parent
        return node.parent

    def delete(self, key):
        node = self.find_node(key)
        if not node.left or not node.right:
            y = node
        else:
            y = self.successor(node)

        if y.left:
            x = y.left
        else:
            x = y.right
        if x:
            x.parent = y.parent
        if not y.parent:
            if x:
                self.root = x
            else:
                # Keep empty tree as the form of  (None,(None, None, None)).
                self.root = BSTreeNode()
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        # if y != node:
        #    node = y
        # print('node:{}'.format(node))
        if y.key != node.key:
            node.key = y.key
            # Copy y's right satellite data to the substituted postion.
            node.value = y.value
          # node.right = y.right
        # print('x:{}'.format(x))
        # print('y:{}'.format(y))
        # print('node:{}'.format(node))
        return None
