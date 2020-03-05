# Project 1 Question 5-a - Python
# Created by Ryan Doherty
# (a)	(5 points)
# Use your recursive implementation of your BST and your iterative implementation of your AVL Tree from Parts 1 and 2 to construct trees using getRandomArray(10,000). 

import question_1_c as BST # Recursive BST
import question_4_c as AVL # AVL Tree
import question_3_a as RA # getRandomArray

arr = RA.getRandomArray(10000)
AVL = AVL.Node(None)
BST = BST.Node(None)

for n in arr:
    BST.insertRec(n)
    AVL.insertIter(n)

print("Trees sucessfully created!")