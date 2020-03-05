# Project 1 Question 3 part b code - Python
# Created by Ryan Doherty

# (b) (3 points) (You must submit code for this question!) Implement a function getSortedArray(n)
# where the output is an array of size n. The 0th element should be equal to n, the
# 1st element should be equal to n-1, and so on.

def getSortedArray(n):
    arr = []
 
    for i in range(n, 0, -1):
        arr.append(i)

    return arr

def printArray(arr):
    for i in arr:
        print(i, end=' ')

if __name__ == "__main__":
    arr = getSortedArray(20)
    printArray(arr)