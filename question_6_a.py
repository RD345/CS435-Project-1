# Project 1 Question 6-a - Python
# Created by Ryan Doherty
# (a)	(5 points) (You must submit code for this question!) Modify your iterative implementations of your methods in AVLTree and BinarySearchTree by keeping track of how many times you traverse one level down in the tree. In other words, if you go from a node to its child, add 1 to the counter.

import time
import question_1_d as BST # Iteritive BST
import test as AVL # AVL Tree
import question_3_a as RA # getRandomArray

def createTree(tree):
    for n in arr:
        tree.insertIter(n)
    return tree

beforeTime = time.perf_counter()
arr = RA.getRandomArray(30000)
print("Time to generate array:", time.perf_counter() - beforeTime)

beforeTime = time.perf_counter()
# avl = createTree(AVL.Node(None))
print("The time to complete the AVL is:", time.perf_counter() - beforeTime)

beforeTime = time.perf_counter()
bst = createTree(BST.Node(None))
print("The time to complete the BST is:", time.perf_counter() - beforeTime)


# print(arr)
# bst.printTree()
