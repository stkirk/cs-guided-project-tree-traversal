# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# given a tree, t, return its node values 
# first value should be the root.value
# following elements should be the values of all level 2 children of root from left to right
# following should be all level 3 values from left to right et cetera
# solution must be iterative
# use breadth first search
from collections import deque
def tree_value_by_level(t):
    # init nodes_by_level list
    nodes_by_level = []
    # if t isn't a node return empty list
    if not t:
        return nodes_by_level
    # init a queue to hold nodes, first item is root value
    q = deque()
    q.append(t)
    # while loop as long as nodes are in the queue
    while len(q) > 0:
        # popleft node from queue into nodes_by_level list
        current_node = q.popleft()
        nodes_by_level.append(current_node.value)
        # if current_node.left (one we just poppped)
        if current_node.left:
            # append it to the queue
            q.append(current_node.left)
        if current_node.right:
            # append it to the queue
            q.append(current_node.right)
    return nodes_by_level

root = Tree(1)
root.left = Tree(2)
root.left.right = Tree(3)
root.right = Tree(4)
root.right.left = Tree(5)

print(tree_value_by_level(root)) # [1,2,4,3,5]
