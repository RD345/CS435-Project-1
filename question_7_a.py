# Project 1 Question 7-a - Python
# Created by Ryan Doherty

# (a)	(3 points) (You must submit code for extra credit on this question!) Use time packages in your respective language to quantify (in milliseconds/picoseconds) how much longer it takes to run 10,000 inserts and 10,000 deletes on a Binary Search Tree versus a Balanced Binary Search Tree.

import time
import question_1_d as BST # Iteritive BST
import question_4_c as AVL # Iteritive AVL Tree
import question_3_a as RA  # getRandomArray

def createTree(tree):
    for n in arr:
        tree.insertIter(n)
    return tree

def deleteTree(tree):
    for n in arr:
        tree.deleteIter(n)
    return tree

avl_time = []
bst_time = []

beforeTime = time.perf_counter()
arr = RA.getRandomArray(10000)
print("Time to generate array:", time.perf_counter() - beforeTime, "ms")


beforeTime = time.perf_counter()
bst = createTree(BST.Node(None))
bst_time.append(1000 * (time.perf_counter() - beforeTime))
print("The time to complete the BST is:", bst_time[0], "ms")

beforeTime = time.perf_counter()
avl = createTree(AVL.Node(None))
avl_time.append(1000 * (time.perf_counter() - beforeTime))
print("The time to complete the AVL is:", avl_time[0], "ms")

beforeTime = time.perf_counter()
bst = deleteTree(BST.Node(None))
bst_time.append(1000 * (time.perf_counter() - beforeTime))
print("The time to delete the BST is:", bst_time[1], "ms")

beforeTime = time.perf_counter()
avl = deleteTree(AVL.Node(None))
avl_time.append(1000 * (time.perf_counter() - beforeTime))
print("The time to delete the AVL is:", avl_time[1], "ms")
