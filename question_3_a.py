# Project 1 Question 3 part a code - Python
# Created by Ryan Doherty
# (5 points) Arrays of Integers
# (a) (2 points) (You must submit code for this question!) Implement a function getRandomArray(n)
# where the output is an array of size n, and contains distinct random numbers (in
# other words, no two numbers in the array should be the same number). Math.rand()
# might be useful here.
import random

def getRandomArray(n):
    arrIn = []
    arrOut = []
 
    for i in range(0, n):
        arrIn.append(i)

    while len(arrIn) > 0:
        i = random.choice(arrIn)
        arrOut.append(i)
        arrIn.remove(i)

    return arrOut

def printArray(arr):
    for i in arr:
        print(i, end=' ')

if __name__ == "__main__":
    arr = getRandomArray(20)
    printArray(arr)