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
    def deleteRec(self, val):
        if self.val:
            if val is self.val:
                # TODO delete curr
                print("Deleted:", val)
            
            elif val < self.val:
                if self.left is None:
                    print("Node not found")
                    return
                else:
                    self.left.deleteRec(val)

            elif val > self.val:
                if self.right is None:
                    print("Node not found")
                    return
                else:
                    self.right.deleteRec(val)
            else:
                print("Node not found")
        else:
            print("tree empty")

    # Finds the next biggest element in the BST recursively:
    def findNextRec(self, val):
        #TODO
        print()

    # Finds the next biggest element in the BST recursively:
    def findPrevRec(self, val):
        #TODO
        print()

    # Finds the minimum value in the BST recursively:
    def findMinRec(self, val):
        #TODO
        print()

    # Finds the maximum value in the BST recursively:
    def findMaxRec(self, val):
        #TODO
        print()

    # Prints the BST recursively In-Order:
    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.val)

        if self.right:
            self.right.printTree()


root = Node(None)
arr_in = [5, 4, 12, 2, 0, 9]
root.insertRec(arr_in[0])
root.insertRec(arr_in[1])
root.insertRec(arr_in[2])
root.insertRec(arr_in[3])
root.insertRec(arr_in[4])
root.insertRec(arr_in[5])

root.deleteRec(4)
root.printTree()