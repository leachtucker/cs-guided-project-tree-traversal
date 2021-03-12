"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()

        print(self.val)

        if self.right is not None:
            self.right.printInOrder()

    def printPreOrder(self):
        print(self.val)

        if self.left is not None:
            self.left.printInOrder()

        if self.right is not None:
            self.right.printInOrder()

def build_tree(preorder, inorder):
    # Preorder input
    root = None

    prevNode = None
    for i in range(0, len(preorder)//2+1, 2):
        currNode = TreeNode(preorder[i])

        leftNode = None
        rightNode = None

        # Create new tree nodes
        if len(preorder)-1 >= i+1:
            leftNode = TreeNode(preorder[i+1])

        if len(preorder)-1 >= i+2:
            rightNode = TreeNode(preorder[i+2])

        # Point our current node to the left and right nodes
        currNode.left = leftNode
        currNode.right = rightNode

        print(f'Current node: {currNode.val}. Left: {currNode.left.val}. Right: {currNode.right.val}')

        # Keep track of the first _currNode_. This is the start of the tree
        if i == 0:
            root = currNode

        if prevNode is not None:
            if currNode.val > prevNode.val:
                prevNode.right = currNode
            else:
                prevNode.left = currNode
        else:
            if root.val > currNode.val:
                root.left = currNode
            else:
                root.right = currNode

    return root



preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

newTree = build_tree(preorder, None)