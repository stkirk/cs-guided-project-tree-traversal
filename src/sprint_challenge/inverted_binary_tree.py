# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# given a root node of a binary tree, invert the tree
# invert meaning flip the right and left pointers of a node
# left child node will now be on right and vice versa
# breadth first traversal: flipping left-> and right->left all the way down
from collections import deque
def inverted_tree(root):
    # init queue with root as only item
    q = deque()
    q.append(root)
    # while loop as long as items in the queue
    while len(q) > 0:
        # init current_node as popleft from queue
        current_node = q.popleft()
        # flip current_nodes pointers
        old_left = current_node.left
        old_right = current_node.right
        current_node.left = old_right
        current_node.right = old_left
        # if current_node.left exists append it to queue
        if current_node.left:
            q.append(current_node.left)
        # if current_node.right exists append it to the queue
        if current_node.right:
            q.append(current_node.right)

    # return something root?
    return root

root = Tree(6)
root.left = Tree(4)
root.left.left = Tree(2)
root.left.right = Tree(5)
root.right = Tree(8)
root.right.left = Tree(7)
root.right.right = Tree(9)

inverted_tree(root)
print(root.right.value) # 4
print(root.left.value) # 8