# Project 1 Question 6-c - Python
# Created by Ryan Doherty
# (c)	(5 points) (You must submit code for this question!) Construct a BST and AVLTree iteratively using getSortedArray(10000). Compare how many levels we have to traverse in the two trees. You can include a screenshot of your code’s output or write it out by hand.

import question_1_d as BST # Iteritive BST
import question_4_c as AVL # AVL Tree
import question_3_b as SA # getSortedArray

def createTree(tree):
    for n in arr:
        tree.insertIter(n)
    return tree

arr = SA.getSortedArray(10000)

avl = createTree(AVL.Node(None))
print("The traversals of the AVL is:", avl.traversals)

bst = createTree(BST.Node(None))
print("The traversals of the BST is:", bst.traversals)