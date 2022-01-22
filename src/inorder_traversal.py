"""
You are given a binary tree.

Write a function that can return the inorder traversal of node values.

Example:
Input:

   3
    \
     1
    / \
   5   9

Output: [3,5,1,9]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Plan:
# depth first traversal, reach leaf first
# Base case for recursion, if root.left and root.right are None bubble back up the tree
# 
def inorder_traversal_recursive(root):
    in_order_nodes = []
    def visit_nodes(node, in_order_nodes):
        # define a base case in helper function
        if node:
            visit_nodes(node.left, in_order_nodes)
            in_order_nodes.append(node.val)
            visit_nodes(node.right, in_order_nodes)
    visit_nodes(root, in_order_nodes)
    return in_order_nodes

# test cases
five = TreeNode(5)
nine = TreeNode(9)
one = TreeNode(1, five, nine)
root = TreeNode(3, None, one)

print(inorder_traversal_recursive(root)) # [3, 5, 1, 9]
