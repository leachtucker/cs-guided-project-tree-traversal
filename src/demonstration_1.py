"""
You are given a binary tree.

Write a function that can return the inorder traversal of node values.

Example:
Input:

   3
    \
     1
    /
   5

Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root, array):
    # Go left
    if root.left is not None:
        inorder_traversal(root.left, array)

    # Evaluate
    array.append(root.val)

    # Go right
    if root.right is not None:
        inorder_traversal(root.right, array)

root = TreeNode(3)
root.right = TreeNode(1)
root.right.left = TreeNode(5)

inOrder = []

inorder_traversal(root, inOrder)

print(inOrder)
