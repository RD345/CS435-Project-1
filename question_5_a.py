# Project 1 Question 5-a - Python
# Created by Ryan Doherty
# (a)	(5 points) (You must submit code for this question!) Use your recursive implementation of your BST and your iterative implementation of your AVL Tree from Parts 1 and 2 to construct trees using getRandomArray(10,000). Both trees must be made from the same array. In other words, do not call the method twice - store the output of the method from getRandomArray(10,000) once and use it to construct both trees.
import question_1_c as BST # Recursive BST
import question_4_c as AVL # AVL Tree
import question_3_a as RA # getRandomArray

arr = RA.getRandomArray(100)
AVL = AVL.Node(None)
BST = BST.Node(None)

for n in arr:
    BST.insertRec(n)
print(arr)
BST.printTree()