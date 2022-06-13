# Copyright th357, jr574, ro46 
# Juni 2022


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
            current = self.root  # setzt current als Wurzel
            parent = None
            # prüft ob Ende des erreicht ist oder ob doppelt daten vorhanden sind
            # current ist aktuelles parent element
            # while current is not None and current.data != data:
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

    def preOrder(self, bst):
        if bst is None:
            pass
        else:
            print(bst.data)
            self.preOrder(bst.left)
            self.preOrder(bst.right)


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
            out = []
            # ! - Problem mit root
            if self.data != type(None):
                if self.data > xmin:
                    self.getrange(self.left, xmin, xmax)
                if (xmin <= self.data) and (self.data <= xmax):
                    out.append(self.data)
                if self.data < xmax:
                    self.getrange(self.right, xmin, xmax)
            return out


if __name__ == "__main__":
    bst = BST()
    bst.insert(7)
    bst.insert(8)
    bst.insert(2)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.preOrder(bst.root)
    print(bst.getrange(2, 8))
