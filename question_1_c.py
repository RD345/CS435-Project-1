# Project 1 Question 1 part c code - Python
# Created by Ryan Doherty
class Node:

    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val

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

    def deleteRec(self, val):
        if self.val:
            if val is self.val:
                # TODO delete curr
                print("Deleting val")
            
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

    def findNextRec(self, val):
        #TODO
        print()

    def findPrevRec(self, val):
        #TODO
        print()

    def findMinRec(self, val):
        #TODO
        print()

    def findMaxRec(self, val):
        #TODO
        print()

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.val),
        if self.right:
            self.right.PrintTree()
root = Node(None)
arr_in = [5, 4, 12, 2, 0, 9]
root.insertRec(arr_in[0])
root.insertRec(arr_in[1])
root.insertRec(arr_in[2])
root.insertRec(arr_in[3])
root.insertRec(arr_in[4])
root.insertRec(arr_in[5])

root.deleteRec(12)
print(root.left.val)