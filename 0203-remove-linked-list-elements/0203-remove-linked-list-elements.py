# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        temp = ListNode(-1)
        temp.next = head
        curr = temp

        while( curr.next != None):
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return temp.next
        