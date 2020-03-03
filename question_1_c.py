# Project 1 Question 1-c - Python
# Created by Ryan Doherty

# (8 points) (You must submit code for part of this question! ) Use the framework
# below to describe how you would recursively implement the following methods of
# a Binary Search Tree. Afterwards, submit an implementation of all of the methods
# in your Github. Note that the Rec suffix simply means that the function is recursive.
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
    def findNextRec(self, start):
        if self.val + 1 is start: # If current is only one larger it must be the next biggest element.
            return self

        elif self.val <= start: # If value is less, go right
            return self.right.findNextRec(start)
            
        elif self.val > start: # If value is greater, go left
            if self.left:
                return self.left.findNextRec(start)
            else:
                return self
        
                

    # Finds the next smallest element in the BST recursively:
    def findPrevRec(self, start):
        if self.val - 1 is start: # If current is only one smaller it must be the next smallest element.
            return self

        elif self.val < start: # If value is less, go right
            if self.right:
                return self.right.findPrevRec(start)
            else:
                return self

        elif self.val >= start and self.left: # If value is greater, go left
            return self.left.findPrevRec(start)


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

        print(self.val, end=' ')

        if self.right:
            self.right.printTree()


root = Node(None)
arr_in = [5, 4, 12, 2, 0, 9, 22, 8, 11]
for n in arr_in:
    root.insertRec(n)

root.printTree()
print()
root.findMinRec()
root.findMaxRec()
print("Next node is:", root.findNextRec(12).val)
print("Previous node is:", root.findPrevRec(4).val)

root.deleteRec(None, 4)
root.printTree()