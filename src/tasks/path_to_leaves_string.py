# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# given a binary tree of nodes with integer values, return all paths from root to leaves as an array of string representations of each path
# return format ["root->node1->node2->noden", ...]
# root and noden should be the values of those nodes

# Plan:
    # depth first traversal using recursion
    # need to keep track of path in a string
    # base case is going to be node with no left or right paths
    # need a helper function to pass in node and copy of path
def root_to_leaves(t):
    # init paths list
    paths_list = []
    # safety check that t is a node
    if not t:
        return paths_list

    # define helper function that takes node and path string=""
    def helper(node, path=""):
        # traversal will be preorder, left path first
        # base case: if node.left and node.right are None
        if node.left is None and node.right is None:
            # we've reached a leaf
            # add node.value to path string
            path += f'{node.value}'
            # individual path should be complete, append to list
            paths_list.append(path)
            return

        # preorder operation: add "node.value->" to path string
        path += f'{node.value}->'

        # left traversal if node.left exists
        if node.left:
            # call helper, pass in node.left and path string
            helper(node.left, path)
        # right traversal if node.right exists
        if node.right:
            # call helper, pass in node.right and path string
            helper(node.right, path)

    # invoke helper, pass in t
    helper(t)
    return paths_list

# test case:
'''
    5
   / \
  2  -3
 / \
10  4
'''
root = Tree(5)
root.left = Tree(2)
root.left.left = Tree(10)
root.left.right = Tree(4)
root.right = Tree(-3)

print(root_to_leaves(root)) # ["5->2->10", "5->2->4", "5->-3"]
