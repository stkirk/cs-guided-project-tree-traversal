# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# Given a linked-list, l, reverse and return it
# In place solution O(1) space
# O(n) time

def reverse_ll(l):
    # init old_node pointer at None
    old_node = None
    # init current_node pointer at head
    current_node = l
    # init next_node as None
    next_node = None

    # while loop as long as current_node is not None
    while current_node:
      # cache current_node.next as next_node
      next_node = current_node.next
      # point current_node backwards to old_node
      current_node.next = old_node
      # cache current_node as old_node
      old_node = current_node
      # reassign current_node to next_node
      current_node = next_node
    
    return old_node


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(reverse_ll(head)) # [5, 4, 3, 2, 1]
