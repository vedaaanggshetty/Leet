# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        
        k = k % n
        if k == 0:
            return head

        new = head
        for _ in range(n - k- 1):
            new = new.next

        temp = new.next
        new.next = None
        curr.next = head

        return temp

        
        