# Project 1 Question 1 part c code - Python
# Created by Ryan Doherty

# (8 points) (You must submit code for part of this question! ) Use the framework
# below to describe how you would recursively implement the following methods of
# a Binary Search Tree. Afterwards, submit an implementation of all of the methods
# in your Github. Note that the Rec sux simply means that the function is recursive.
# 1. insertRec
# 2. deleteRec
# 3. findNextRec
# 4. findPrevRec
# 5. findMinRec
# 6. findMaxRec
 

class Node:

    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val

    # Inserts a value into the BST recursively:
    def insertRec(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insertRec(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insertRec(val)
        else:
            self.val = val
            
    # Deletes a value in the BST recursively:
    def deleteRec(self, parent, val):
        if self.val:
            if val is self.val: # Delete the current node
                print("Deleted:", self.val)
                if self.left:
                    if self.right:
                        # TODO: find next node to swap
                        print()
                    else:
                        if parent:
                            if parent.left is self:
                                parent.left = self.left
                            elif parent.right is self:
                                parent.right = self.right
                else:
                    self = None
            
            elif val < self.val:
                if self.left is None:
                    print("Node not found")
                    return
                else:
                    self.left.deleteRec(self, val)

            elif val > self.val:
                if self.right is None:
                    print("Node not found")
                    return
                else:
                    self.right.deleteRec(self, val)
            else:
                print("Node not found")
        else:
            print("Tree is empty")

    # Finds the next biggest element in the BST recursively:
    def findNextRec(self, val):
        # TODO
        if self:
            if self + 1 is val: # If current is only one larger it must be the next biggest element.
                return self
            if self.right:
                self.right.findNextRec(val)
            # TODO
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insertRec(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insertRec(val)
        else:
            self.val = val

    # Finds the next smallest element in the BST recursively:
    def findPrevRec(self, val):
        # TODO
        print()

    # Finds the minimum value in the BST recursively:
    def findMinRec(self):
        if self.left is None:
            print("Min value is:", self.val)
        else:
            self.left.findMinRec()

    # Finds the maximum value in the BST recursively:
    def findMaxRec(self):
        if self.right is None:
            print("Max value is:", self.val)
            return self.val
        else:
            self.right.findMaxRec()

    # Prints the BST recursively In-Order:
    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.val)

        if self.right:
            self.right.printTree()


root = Node(None)
arr_in = [5, 4, 12, 2, 0, 9, 22, 8, 11]
for n in arr_in:
    root.insertRec(n)

root.findMinRec()
root.findMaxRec()

root.deleteRec(None, 4)
root.printTree()