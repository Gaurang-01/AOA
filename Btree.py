class Node:
    def __init__(self, leaf=True):
        self.keys = []
        self.child = []
        self.leaf = leaf

class BTree:
    def __init__(self, t=2):
        self.root = Node()
        self.t = t

    def insert(self, key):
        root = self.root

        if len(root.keys) == 2*self.t-1:
            new = Node(False)
            new.child.append(root)
            self.split(new, 0)
            self.root = new

        self.add(self.root, key)

    def split(self, node, i):
        t = self.t
        y = node.child[i]
        z = Node(y.leaf)

        mid = y.keys[t-1]
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]

        if not y.leaf:
            z.child = y.child[t:]
            y.child = y.child[:t]

        node.child.insert(i+1, z)
        node.keys.insert(i, mid)

    def add(self, node, key):
        i = len(node.keys)-1

        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.child[i].keys) == 2*self.t-1:
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1

            self.add(node.child[i], key)

    def display(self, node=None):
        if node is None:
            node = self.root

        print(node.keys, end=" ")

        for child in node.child:
            self.display(child)
tree = BTree()
for x in [10, 20, 5, 6, 12, 30, 7, 17]:
    tree.insert(x)

tree.display()