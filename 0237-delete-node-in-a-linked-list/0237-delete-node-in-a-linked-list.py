# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        # not at last and no head...interesting

        node.val = node.next.val
        node.next = node.next.next          