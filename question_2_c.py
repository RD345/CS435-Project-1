# Project 1 Question 2 part c code - Python
# Created by Ryan Doherty

def form_bst(root, num_list):
    for i in num_list:
        root.insert(i)

    for i in num_list:
        if root.value:
            print("null")

class Node:
    def __int__(self, val):

        self.value = val
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


root = Node()
arr_in = [5, 4, 12, 2, 0, 9]
form_bst(root, arr_in)