# class for individual node in the Binary Tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # init new node with value passed in
        new_node = BSTNode(value)
        # find where the value should be in the tree
        if value <= self.value:
            # check if child exists
            if self.left is None:
                self.left = new_node
            else:
                # move the job of inserting down a level
                self.left.insert(value)
        else:
            # the value must go right
            if self.right is None:
                self.right = new_node
            else:
                # move the job of inserting down a level
                self.right.insert(value)

'''
Depth First Traversal: must go all the way down a path to the bottom
    - This is a consequence of using recursion
    - Uses a stack
        - Either the call stack (recursive)
        - Or a user-defined stack (iterative)
'''

# function to print the tree starting at the root
# depth first, preorder goes through left branch first, visiting each node on way down tree
# visiting node === performing desired operation on the node
# in this case that is the print function
def print_tree_preorder(root):
    print(root.value)
    # if we have a left child node
    if root.left:
        print_tree_preorder(root.left)

    # if we have a left child node
    if root.right:
        print_tree_preorder(root.right)

# depth first, in order
# vists nodes all the way down and to the left, then works way back up visiting right child nodes on the way
# in BST would visit nodes from smallest value to largest value
def print_tree_inorder(root):
    # if we have a left child node
    if root.left:
        print_tree_inorder(root.left)

    print(root.value)

    # if we have a left child node
    if root.right:
        print_tree_inorder(root.right)

# depth first, postorder
# travels down left branch and visits lowest child nodes first works back up left then goes down right visits lowest level child nodes works its way back up and visits ROOT LAST
def print_tree_postorder(root):
    # if we have a left child node
    if root.left:
        print_tree_postorder(root.left)

    # if we have a left child node
    if root.right:
        print_tree_postorder(root.right)

    print(root.value)

'''
MAIN DIFFERENCE of different depth searches: 
    The order of the nodes you want to perform an operation on
'''

'''
Iterative depth first traversal: make our own stack instead of using the call stack through recursion
This is preorder, any other order isn't easy to do
'''
def iterative_dft(root):
    stack = []
    stack.append(root)

    while len(stack) > 0:
        # remove item on top of stack (starts with root)
        current_node = stack.pop()
        # evalutate it, in this case print
        print(current_node.value)

        # add next nodes onto stack
        # want to vist left branch first, add right branch to bottom of stack
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)


'''
Breadth First Search: iterative version of tree traversal
Uses a queue instead of recursion(essentially uses a stack)
'''
def breadth_first_traversal(root):
    queue = []
    queue.append(root)

    while len(queue) > 0:
        # pop from front
        current_node = queue.pop(0)
        # perform operation here
        print(current_node.value)
        # add next level nodes to back of the queue
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

'''
test case tree
              8
           /     \
          5       12
        /  \     /   \
       1    7   9     14
'''
root = BSTNode(8)
root.insert(5)
root.insert(12)
root.insert(1)
root.insert(7)
root.insert(9)
root.insert(14)

print("-----preorder-----")
print_tree_preorder(root)

print("-----inorder-----")
print_tree_inorder(root)

print("-----postorder-----")
print_tree_postorder(root)

print("-----iterative depth first-----")
iterative_dft(root)

print("-----breadth first-----")
breadth_first_traversal(root)
