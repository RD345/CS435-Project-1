# Project 1 Question 7-a - Python
# Created by Ryan Doherty

# (a)	(3 points) (You must submit code for extra credit on this question!) Use time packages in your respective language to quantify (in milliseconds/picoseconds) how much longer it takes to run 10,000 inserts and 10,000 deletes on a Binary Search Tree versus a Balanced Binary Search Tree.

import time
import question_1_d as BST # Iteritive BST
import question_4_c as AVL # AVL Tree
import question_3_a as RA # getRandomArray

def createTree(tree):
    for n in arr:
        tree.insertIter(n)
    return tree

beforeTime = time.perf_counter()
arr = RA.getRandomArray(30000)
print("Time to generate array:", time.perf_counter() - beforeTime)

beforeTime = time.perf_counter()
avl = createTree(AVL.Node(None))
print("The time to complete the AVL is:", time.perf_counter() - beforeTime)

beforeTime = time.perf_counter()
bst = createTree(BST.Node(None))
print("The time to complete the BST is:", time.perf_counter() - beforeTime)


# print(arr)
# bst.printTree()
