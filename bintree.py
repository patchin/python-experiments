class BinTree(object):
    def __init__(self):
        self.root = None
    def insert(self, number):
        if self.root == None:
            self.root = Node(number)
        else:
            self.root.insert(number)
    def print(self):
        if self.root != None:
            self.root.print()
        else:
            print("No tree.")

class Node(object):
    def __init__(self, number):
        self.left = None
        self.right = None
        self.value = number
    def value(self):
        return self.value
    def insert(self, number):
        if number > self.value:
            if self.right != None:
                self.right.insert(number)
            else:
                self.right = Node(number)
        else:
            if self.left != None:
                self.left.insert(number)
            else:
                self.left = Node(number)
    def print(self):
        if self.left != None:
            self.left.print()
        print("value:" + str(self.value))
        if self.right != None:
            self.right.print()

tree = BinTree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(345)
tree.insert(-3)
tree.insert(10)
tree.print()
