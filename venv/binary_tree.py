class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def insertNode(self, data):
        if self.data:
            if self.data < data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data)
            else:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data = data

    def invertTree(self):
        if self.data:
            if self.left and self.right:
                self.left.invertTree()
                self.right.invertTree()
                swap(self.left, self.right)
            elif self.left and not self.right:
                self.right = self.left
                self.left = None
                self.right.invertTree()
            elif self.right and not self.left:
                self.left = self.right
                self.right = None
                self.left.invertTree()

def swap(n1:Node, n2:Node):
    temp = n1.data
    n1.data = n2.data
    n2.data = temp

if __name__ == "__main__":
    root = Node(5)
    root.insertNode(7)
    root.insertNode(2)
    root.insertNode(4)
    root.insertNode(9)
    root.insertNode(13)
    root.insertNode(3)
    root.insertNode(12)
    root.insertNode(15)
    root.insertNode(8)
    root.insertNode(1)
    root.printTree()
    root.invertTree()
    print("Inverted")
    root.printTree()
