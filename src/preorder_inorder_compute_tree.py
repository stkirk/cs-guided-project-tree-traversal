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

def build_tree(preorder, inorder):
    # base case: when we've gone through the entire inroder list, we've constructed the entire tree
    if not inorder:
        return
    # figure out what the root is
    # preorder traversal always visits the root first
    root = TreeNode(preorder[0])
    # find root index in inorder list
    root_idx = inorder.index(root.val)
    # everything from the beginning of inorder list up to root_idx is in the left subtree
    # move closer to the base case by slicing fown the two lists and passing them in recursively to this function
    root.left = build_tree(preorder[1:], inorder[0:root_idx])


    # recursively build the left sub-tree


    # recursively build the right sub-tree

    # return the root
    return root

