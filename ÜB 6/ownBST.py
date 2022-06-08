# Copyright Robin Obliers 
# Juni 2020 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, data):
        if self.data: 
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def __repr__(self) -> str:
        if self.left:
            self.left.__repr__()
        print (self.node)
        if self.right:
            self.right.__repr__()
        
        
if __name__ == "__main__":
    #root = Node(2)
    bst = BST() 
    bst.insert(Node(7, None, None))
    bst.insert(Node(3, None, None))

    print(str(bst))