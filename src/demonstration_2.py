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

    # BFS -- returns an array representing the preorder breadth-first traversal of the tree
    def preorder(self, array=[]):
        queue = []

        queue.append(self)
        while len(queue) > 0:
            currNode = queue.pop(0)

            # Eval curr node
            array.append(currNode.val)

            # Add children to the queue
            if currNode.left is not None:
                queue.append(currNode.left)

            if currNode.right is not None:
                queue.append(currNode.right)

        return array

def build_tree(preorder, inorder):
    return helper(0, 0, len(inorder)-1, preorder, inorder)

# Built this iteratively and then used online resources to build a recursive method
def helper(preStart, startIdx, endIdx, preorder, inorder):
    if preStart > len(preorder) - 1 or startIdx > endIdx:
        return None

    root = TreeNode(preorder[preStart])

    inorderIdx = inorder.index(root.val)

    root.left = helper(preStart + 1, startIdx, inorderIdx-1, preorder, inorder)
    root.right = helper(preStart + inorderIdx - startIdx + 1, inorderIdx+1, endIdx, preorder, inorder)

    return root

preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

newTree = build_tree(preorder, inorder)
preOrderArr = newTree.preorder()

print(preOrderArr)