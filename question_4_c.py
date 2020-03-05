# Project 1 Question 4-c - Python
# Created by Ryan Doherty

# (c)	(15 points) You must submit code for this question!) Submit an implementation of the following iterative methods in an AVL Tree. You do not need to submit written answers to the framework from above, but it might be useful for you to consider the answers to those questions when writing code. Note that the Iter suffix simply means that the function is iterative. Keep in mind that an iterative solution cannot make a single recursive call! You will need to use your implementation of Node from the previous question.
# 1.	insertIter
# 2.	deleteIter
# 3.	findNextIter
# 4.	findPrevIter
# 5.	findMinIter
# 6.	findMaxIter

import question_1_d as BST # Iteritive BST

debug = False

class Node(BST.Node):

    def __init__(self, val, height = 0):

        self.left = None
        self.right = None
        self.val = val
        self.height = height
        self.traversals = 0

    def updateHeights(self, nodes):
        curr = self
        
        for n in nodes:
            if curr.val is n:
                pass
            elif curr.left and curr.left.val is n:
                curr = curr.left
                self.traversals += 1 # Add to traversals
            elif curr.right and curr.right.val is n:
                curr = curr.right
                self.traversals += 1 # Add to traversals

            if curr.left:
                if curr.right:
                    curr.height = 1 + max(curr.left.height, curr.right.height) 
                else:
                    curr.height = 1 + curr.left.height

            elif curr.right:
                curr.height = 1 + curr.right.height
                

    # Inserts a value into the BST Iterively:
    def insertIter(self, val):
        inserted = False
        curr = self
        # balance = 0
        parents = [] # Holds the nodes of the parents
      

        def bal(self):
            curr = self

            if curr.left:
                if curr.right:
                    balance = curr.left.height - curr.right.height
                else:
                    balance = curr.height # No right child

            elif curr.right:
                balance = curr.height # No left child
            
            if debug:
                print("V:", val, 'H:', curr.height, 'B:', balance)

            while abs(balance) > 1:
                # Case Left Left 
                if balance > 1 and val < curr.left.val: 
                    return curr.rightRotate() 
        
                # Case Right Right 
                if balance < -1 and val > curr.right.val: 
                    return curr.leftRotate() 
        
                # Case Left Right 
                if balance > 1 and val > curr.left.val: 
                    curr.left = curr.leftRotate() 
                    return curr.rightRotate() 
        
                # Case Right Left 
                if balance < -1 and val < curr.right.val: 
                    curr.right = curr.rightRotate() 
                    return curr.leftRotate()

        # Perform BST insert:
        if not curr.val:
            self.val = val
        else:
            while not inserted:
                if val < curr.val:
                    parents.append(curr.val) # Remember parent

                    if curr.left is None:
                        curr.left = Node(val)
                        # bal(curr, True)
                        inserted = True
                    else:
                        self.traversals += 1 # Add to traversals
                        curr = curr.left
                elif val > curr.val:
                    if curr.right is None:
                        curr.right = Node(val)
                        # bal(curr, False)
                        inserted = True
                    else:
                        self.traversals += 1 # Add to traversals
                        curr = curr.right
            if debug:
                print(parents)
            self.updateHeights(parents)
            bal(curr)
            
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
                self.traversals += 1 # Add to traversals
                curr = curr.left # Move left

            elif val > curr.val:
                parent = curr
                self.traversals += 1 # Add to traversals
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
                            self.traversals += 1 # Add to traversals
                            curr = curr.left # Move left

                        elif temp.val > curr.val:
                            curr.val = temp.val # Set the current node's value to the sucessor.
                            parent = curr
                            self.traversals += 1 # Add to traversals
                            curr = curr.right # Move right
                        val = temp.val # Continues the delete with the sucessor as the new target.
                    else:
                        # curr = None
                        if parent.left is curr: # If current is a left child:
                            parent.left = None

                        elif parent.right is curr: # If current is a right child:
                            parent.right = None 
                        return


    def printTreeDiagram(self):
        tree = []
        max_height = self.height

        def printTreeDiagramHelper(self):
            for h in range(0, self.height):
                tree.append('')

            if self.left:
                printTreeDiagramHelper(self.left)
                
            tree[self.height] += self.height * ' ' + ' ' + str(self.val) + max_height * ' '

            if self.right:
                printTreeDiagramHelper(self.right)

        
        printTreeDiagramHelper(self)
        tree.reverse()
        if debug:
            for layer in tree:
                print(layer)
    
    # Function to get the balance of the node its called on. negative values < -1 are left-unbalanced,
    # positive values > 1 are right unbalanced.
    def getBal(self, root):
        if not root:
            return 0
        return root.findMaxIter().height - root.findMinIter().height

    def rightRotate(self):
        if debug:
            print("RR")

    def leftRotate(self):
        if debug:
            print("LL")

if __name__ == "__main__":
    debug = True
    avl = Node(None)
    arr_in = [5, 4, 12, 2, 0, 9, 22, 8, 11, 1, 3, 7]
    for n in arr_in:
        avl.insertIter(n) # 1. insertIter
    avl.printTree()
    print()

    print("Min value is:", avl.findMinIter().val) # 5. findMinIter
    print("Max value is:", avl.findMaxIter().val) # 6. findMaxIter
    print("Next node is:", avl.findNextIter(5).val) # 3. findNextIter
    print("Previous node is:", avl.findPrevIter(9).val) # 4. findPrevIter
    # avl.deleteIter(11) # 2. deleteIter
  
    avl.printTreeDiagram()
    # print(avl.left.getBal(avl))