# Copyright Robin Obliers 
# Juni 2020 


from turtle import left


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__ (self):
        return str(self.data)


class BST(object):
    def __init__(self, root=None) -> None:
        self.root = root # settet root bei jeder Initialisierung = None 

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, parent=None, left = None, right=None)
        else:
            current = self.root  #setzt current als Wurzel
            parent = None 
            # prüft ob Ende des erreicht ist oder ob doppelt daten vorhanden sind
            # current ist aktuelles parent element 
            while current is not None and current.data != data: 
                parent = current 
                if data < current.data: 
                    current = current.left
                else:
                    current = current.right 

            # Schlüssel ist noch nicht im Baum -> auf linker seite einfügen 
            if current is None: 
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

    def preOrder(self, bst):
        if bst is None:
            pass
        else:
            print(bst.data)
            self.preOrder(bst.left)
            self.preOrder(bst.right)


        """
        if self.left:
            self.left.__repr__()
        print (self.node)
        if self.right:
            self.right.__repr__()
        """

def getrange(self, xmin, xmax):
        '''
            returns all keys x with xmin <= x < x max.

            Implementation hints: May use either additional
            parameters or call a recursive subfunction with
            additional parameters.

            Parameters:
                xmin - lower bound (including)
                xmax - upper bound (excluding)

            Returns:
                List of keys with xmin <= x < xmax

            Unit tests:
                >>> bst = BST()
                >>> bst.insert(3); bst.insert(1); bst.insert(6)
                >>> bst.insert(2); bst.insert(5); bst.insert(4)
                >>> sorted(bst.getrange(2, 5))
                [2, 3, 4]
        '''
        if self.data is not None:
            if self.data:
                pass
        
if __name__ == "__main__":
    bst = BST()
    bst.insert(7)
    bst.insert(8)
    bst.insert(2)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.preOrder(bst.root)