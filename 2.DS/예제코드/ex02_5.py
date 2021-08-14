class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

if __name__=="__main":
    root = Node(10)

    root.left = Node(34)
    root.right = Node(89)
    root.left.left = Node(45)
    root.left.right = Node(50)