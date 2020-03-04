# Project 1 Question 6-a - Python
# Created by Ryan Doherty
# (a)	(5 points) (You must submit code for this question!) Modify your iterative implementations of your methods in AVLTree and BinarySearchTree by keeping track of how many times you traverse one level down in the tree. In other words, if you go from a node to its child, add 1 to the counter.

import timeit
import time
import question_1_d as BST # Iteritive BST
import test as AVL # AVL Tree
import question_3_a as RA # getRandomArray

def createTree(tree):
    for n in arr:
        tree.insertIter(n)
    return tree


arr = RA.getRandomArray(10000)
# avl = AVL.Node(None)
# bst = BST.Node(None)

beforeTime = time.perf_counter()
# avl = createTree(AVL.Node(None))
avl_time = time.perf_counter() - beforeTime

beforeTime = time.perf_counter()
bst = createTree(BST.Node(None))
bst_time = time.perf_counter() - beforeTime


# print(arr)
# bst.printTree()

print("The time to complete the BST is:", bst_time)
print("The time to complete the AVL is:", avl_time)