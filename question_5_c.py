# Project 1 Question 5-c - Python
# Created by Ryan Doherty
# (c)	(5 points) 
# Use your iterative implementations of your AVL Tree and BST from Parts 1 and 2 to construct trees from the input of your implementation of getRandomArray(10,000). Both trees must be made from the same array. 

import question_1_d as BST # Iteritive BST
import question_4_c as AVL # AVL Tree
import question_3_a as RA # getRandomArray

arr = RA.getRandomArray(10000)
AVL = AVL.Node(None)
BST = BST.Node(None)

for n in arr:
    BST.insertIter(n)
    AVL.insertIter(n)

print("Trees sucessfully created!")