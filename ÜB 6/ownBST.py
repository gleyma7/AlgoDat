# Copyright Robin Obliers 
# Juni 2020 

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self, root=None) -> None:
        self.root = root # settet root bei jeder Initialisierung = None 

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, parent=None, left = None, right=None)
        else:
            current = self.root #setzt current als Wurzel
            parent = None 
            # prüft ob Ende des erreicht ist oder ob doppelt daten vorhanden sind
            # current ist aktuelles parent element 
            while current is not None and current.data != data: 
                parent = current 
                if data < current.data: 
                    current = current.left
                else
                    current = current.right 

            # Schlüssel ist noch nicht im Baum -> auf linker seite einfügen 
            if current.data is None: 
                if data < parent.data:
                    parent.left = Node(data, parent, None, None)
                else:
                    parent.right = Node(data, parent, None, None)
                    
 '''
        if self.data: 
            if data < self.data: # wenn 
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
'''

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