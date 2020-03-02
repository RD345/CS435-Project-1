# Project 1 Question 4-c - Python
# Created by Ryan Doherty

# (c)	(15 points) You must submit code for this question!) Submit an implementation of the following iterative methods in an AVL Tree. You do not need to submit written answers to the framework from above, but it might be useful for you to consider the answers to those questions when writing code. Note that the Iter suffix simply means that the function is iterative. Keep in mind that an iterative solution cannot make a single recursive call! You will need to use your implementation of Node from the previous question.
# 1.	insertIter
# 2.	deleteIter
# 3.	findNextIter
# 4.	findPrevIter
# 5.	findMinIter
# 6.	findMaxIter


class Node:

    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val

    # Inserts a value into the BST Iterursively:
    def insertIter(self, val):
        curr = self
        inserted = False

        if curr.val:
            while not inserted:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = Node(val)
                        inserted = True
                    else:
                        curr = curr.left
                elif val > curr.val:
                    if curr.right is None:
                        curr.right = Node(val)
                        inserted = True
                    else:
                        curr.right = Node(val)
        else:
            self.val = val
            
    # Deletes a value in the BST Iterursively:
    def deleteIter(self, parent, val):
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
                    self.left.deleteIter(self, val)

            elif val > self.val:
                if self.right is None:
                    print("Node not found")
                    return
                else:
                    self.right.deleteIter(self, val)
            else:
                print("Node not found")
        else:
            print("Tree is empty")

    # Finds the next biggest element in the BST Iterursively:
    def findNextIter(self, start, nextNode):
        if nextNode is None:
            nextNode = self

        if self.val + 1 is start: # If current is only one larger it must be the next biggest element.
            return nextNode

        elif self.val < start and self.right: # If value is less, go right
            return self.right.findNextIter(start, nextNode)

        elif self.val > start: # If value is greater, go left
            if nextNode.val > self.val:
                nextNode = self
            if self.left:
                return self.left.findNextIter(start, nextNode)

        print(nextNode.val, end=' ')
        
                

    # Finds the next smallest element in the BST Iterursively:
    def findPrevIter(self, start, prevNode):
        if self:
            if prevNode is None:
                prevNode = Node(0)

            if self.val - 1 is start: # If current is only one smaller it must be the next smallest element.
                prevNode = self
                return prevNode

            elif self.val < start: # If value is less, go right
                if prevNode.val < self.val:
                    prevNode = self
                if self.right:
                    return self.right.findPrevIter(start, prevNode)

            elif self.val > start and self.left: # If value is greater, go left
                return self.left.findPrevIter(start, prevNode)

        return self

    # Finds the minimum value in the BST Iterursively:
    def findMinIter(self):
        if self.left is None:
            print("Min value is:", self.val)
        else:
            self.left.findMinIter()

    # Finds the maximum value in the BST Iterursively:
    def findMaxIter(self):
        if self.right is None:
            print("Max value is:", self.val)
            return self.val
        else:
            self.right.findMaxIter()

    # Prints the BST Iterursively In-Order:
    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.val, end=' ')

        if self.right:
            self.right.printTree()

    def rightRotate(self):
        print()

    def leftRotate(self):
        print()


avlTree = Node(None)
arr_in = [5, 4, 12, 2, 0, 9, 22, 8, 11]
for n in arr_in:
    avlTree.insertIter(n)

avlTree.printTree()
print()
avlTree.findMinIter()
avlTree.findMaxIter()
print("Next node is:", avlTree.findNextIter(12, None).val)
print("Previous node is:", avlTree.findPrevIter(4, None).val)

avlTree.deleteIter(None, 4)
avlTree.printTree()