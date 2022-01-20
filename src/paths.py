# class for individual node in the Binary Tree
# from binary_tree_traversals import BSTNode

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

# return an array with paths from root to every leaf node
# path --> [8, 5, 1]

def find_paths_recursive(root):
    # create outer scoped variable from helper function to accumulate all the apprended paths
    all_paths = []

    def helper(root, current_path=[]): #gives current_path parameter a default value
        # pre order operation goes here, we want to return the path from top node to bottom leaf
        current_path.append(root.value)
        # base case: if we are at a leaf node, return the current path
        if root.left is None and root.right is None:
            all_paths.append(current_path)
        # this block traverses the whole tree
        if root.left:
            helper(root.left, current_path.copy()) # copy so children add themselves to a new array
        if root.right:
            helper(root.right, current_path.copy())

    # invoke the helper function
    helper(root)
    return all_paths

def find_paths_iterative(root):
    stack = []
    stack.append((root, []))

    all_paths = []

    while len(stack) > 0:
        # remove item on top of stack (starts with root)
        current_node, path = stack.pop()
        path.append(current_node.value)
        # evalutate it, in this case add paths to all_paths when reach a leaf node
        if current_node.left is None and current_node.right is None:
            all_paths.append(path)

        # add next nodes onto stack
        # want to vist left branch first, add right branch to bottom of stack
        if current_node.right:
            stack.append((current_node.right, path.copy()))
        if current_node.left:
            stack.append((current_node.left, path.copy()))

    return all_paths

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

print(find_paths_recursive(root))
print("-----dft iterative-----")
print(find_paths_iterative(root))
