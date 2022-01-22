# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# given a BST, return the sum of all the values between the upper and lower bound parameters
# both bounds are inclusive

def sum_bw_upper_lower(root, lower, upper):
    # init values_to_sum counter
    nodes_sum = 0
    # traverse through the tree with helper function, pass in a node
    def helper(node):
        # if the node.value is >= lower and <= upper\
        if node.value >= lower and node.value <= upper:
            # add node.value to nodes_sum
            nonlocal nodes_sum 
            nodes_sum += node.value

        # traverse left subtree if it exists
        if node.left:
            # run helper passing in node.left
            helper(node.left)
        # traverse the right subree if it exists
        if node.right:
            # run helper passing in node.right
            helper(node.right)

    # invoke helper function passing in root as node
    helper(root)
    # return sum of all values in the list
    return nodes_sum

root = Tree(10)
root.left = Tree(5)
root.left.left = Tree(3)
root.left.right = Tree(7)
root.right = Tree(15)
root.right.right = Tree(18)

print(sum_bw_upper_lower(root, 7, 15)) # 32