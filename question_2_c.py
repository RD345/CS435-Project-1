# Project 1 Question 2 part c code - Python
# Created by Ryan Doherty

# Using the properties of a BST can make creating a sorted list very easy. Since we
# know that: left < root < right, we can simply do an In-order traversal to print a list of 
# increasing value. If we start with an unsorted list, we just feed that data into a new 
# binary tree, then perform the In-order traversal.

# (5 points) (You must submit code for this question! ) Implement the algorithm that
# you described above in sort().

# My Node class from earlier questions can implement this:
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
            
    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.val, end=' ')

        if self.right:
            self.right.printTree()

if __name__ == "__main__":
    root = Node(None)
    arr_in = [5, 4, 12, 2, 0, 9, 58, 82, 6, 44, 25]
    for n in arr_in:
        root.insertRec(n)

    root.printTree()