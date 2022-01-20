# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# given a root node, return the binary tree's nodes using an inorder traversal
# return inorder nodes in a list

def visit_nodes_inorder(root):
    # init inorder_nodes list to append nodes to
    inorder_nodes = []
    # define helper function that takes the root and uses recursion to traverse the tree
    def helper(node):
        # recurse left if node.left exists
        if node.left:
            helper(node.left)
        # append the node
        inorder_nodes.append(node.value)
        # recurse right if node.right exists
        if node.right:
            helper(node.right)

    # run helper function on root
    helper(root)
    return inorder_nodes

root = Tree(2)
root.right = Tree(3)
root.right.left = Tree(4)
print(visit_nodes_inorder(root)) # [2, 4, 3]