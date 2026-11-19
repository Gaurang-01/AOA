
class Node:
    def __init__(self, leaf=True):
        self.keys = []
        self.child = []
        self.leaf = leaf
        self.next = None
class BPlusTree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        result = self.add(self.root, key)

        if result:
            mid, right = result
            new = Node(False)
            new.keys = [mid]
            new.child = [self.root, right]
            self.root = new

    def add(self, node, key):
        if node.leaf:
            if key in node.keys:
                return None

            node.keys.append(key)
            node.keys.sort()

            if len(node.keys) > 3:
                mid = 2
                right = Node()
                right.keys = node.keys[mid:]
                node.keys = node.keys[:mid]

                right.next = node.next
                node.next = right

                return right.keys[0], right

        else:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1

            result = self.add(node.child[i], key)

            if result:
                mid, right = result
                node.keys.insert(i, mid)
                node.child.insert(i+1, right)

                if len(node.keys) > 3:
                    mid = node.keys[2]
                    new = Node(False)

                    new.keys = node.keys[3:]
                    new.child = node.child[3:]

                    node.keys = node.keys[:2]
                    node.child = node.child[:3]

                    return mid, new

        return None
    def display(self):
        node = self.root

        while not node.leaf:
            node = node.child[0]

        print("Leaf nodes:")
        while node:
            print(node.keys, end=" -> ")
            node = node.next
# Main
tree = BPlusTree()

n = int(input("Enter number of keys: "))
arr = list(map(int, input("Enter keys: ").split()))

for x in arr:
    tree.insert(x)

tree.display()
