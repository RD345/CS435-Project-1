# Project 1 Question 1-d - Python
# Created by Ryan Doherty

# (8 points) (You must submit code for this question! ) Submit an implementation
# of the following iterative methods in a Binary Search Tree. You do not need to
# submit written answers to the framework from above, but it might be useful for
# you to consider the answers to those questions when writing code. Note that the
# Iter suffix simply means that the function is iterative. Keep in mind that an
# iterative solution cannot make a single recursive call!
# 1. insertIter
# 2. deleteIter
# 3. findNextIter
# 4. findPrevIter
# 5. findMinIter
# 6. findMaxIter

class Node:

    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val

    # Inserts a value into the BST Iterively:
    def insertIter(self, val):
        inserted = False
        curr = self

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
                        curr = curr.right
            
        else:
            self.val = val
            
    # Deletes a value in the BST Iterively:
    def deleteIter(self, val):
        curr = self
        parent = self
        print("Deleting:", val)

        while val:
            # Base:
            if curr is None:
                print(val, "not found.")
                return self

            # Search for the value:
            elif val < curr.val:
                parent = curr
                curr = curr.left # Move left

            elif val > curr.val:
                parent = curr
                curr = curr.right # Move right

            else: # Delete the current node
                # If a leaf:
                if curr.left is None and curr.right is None: 
                    # Delete it
                    if parent.left is curr: # If curr is left child:
                        parent.left = None
                    elif parent.right is curr: # If curr is right child:
                        parent.right = None
                    return self
                    
                # If only one child:
                elif curr.left is None or curr.right is None: 
                    if parent.left is curr: # If current is a left child:
                        if curr.left:
                            parent.left = curr.left # Parent's left becomes current's left.
                            curr = None
                        elif curr.right:
                            parent.left = curr.right # Parent's left becomes current's right.
                            curr = None
                    elif parent.right is curr: # If current is a right child:
                        if curr.left:
                            parent.right = curr.left # Parent's right becomes current's left.
                        elif curr.right:
                            parent.right = curr.right # Parent's right becomes current's right.
                    return self

                # If two children:
                else:
                    if self.findNextIter(curr.val):
                        temp = self.findNextIter(curr.val) # Find the sucessor.
                        
                        if temp.val < curr.val:
                            curr.val = temp.val # Set the current node's value to the sucessor.
                            parent = curr
                            curr = curr.left # Move left

                        elif temp.val > curr.val:
                            curr.val = temp.val # Set the current node's value to the sucessor.
                            parent = curr
                            curr = curr.right # Move right
                        val = temp.val # Continues the delete with the sucessor as the new target.
                    else:
                        # curr = None
                        if parent.left is curr: # If current is a left child:
                            parent.left = None

                        elif parent.right is curr: # If current is a right child:
                            parent.right = None 
                        return

    # Finds the next biggest element in the BST Iterively:
    def findNextIter(self, start):
        curr = self
        
        while True:
            if curr is None:
                return curr

            elif curr.val + 1 is start: # If curr is only one larger it must be the next biggest element.
                return curr

            elif curr.val <= start: # If value is less, go right
                curr = curr.right

            elif curr.val > start: # If value is greater, go left
                if curr.left:
                    curr = curr.left
                else:
                    return curr
        

    # Finds the next smallest element in the BST Iterively:
    def findPrevIter(self, start):
        curr = self
        
        while True:
            if curr is None:
                return curr

            elif curr.val - 1 is start: # If curr is only one larger it must be the next biggest element.
                return curr

            elif curr.val < start: # If value is less, go right
                if curr.right:
                    curr = curr.right
                else:
                    return curr

            elif curr.val >= start: # If value is greater, go left
                curr = curr.left

    # Finds the minimum value in the BST Iterively:
    def findMinIter(self):
        curr = self

        while True:
            if curr.left is None:
                return curr
            else:
                curr = curr.left

    # Finds the maximum value in the BST Iterively:
    def findMaxIter(self):
        curr = self

        while True:
            if curr.right is None:
                return curr
            else:
                curr = curr.right

    # Prints the BST In-Order:
    def printTree(self):
        if self.left:
            self.left.printTree()
            
        print(self.val, end=' ')

        if self.right:
            self.right.printTree()

if __name__ == "__main__":
    root = Node(None)
    arr_in = [5, 4, 12, 2, 0, 9, 22, 8, 11]
    for n in arr_in:
        root.insertIter(n) # 1. insertIter
    root.printTree()
    print()

    print("Min value is:", root.findMinIter().val) # 5. findMinIter
    print("Max value is:", root.findMaxIter().val) # 6. findMaxIter
    print("Next node is:", root.findNextIter(5).val) # 3. findNextIter
    print("Previous node is:", root.findPrevIter(9).val) # 4. findPrevIter
    root.deleteIter(4) # 2. deleteIter

    root.printTree()