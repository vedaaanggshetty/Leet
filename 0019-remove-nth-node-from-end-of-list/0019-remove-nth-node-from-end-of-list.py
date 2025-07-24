# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # dummy = ListNode(0)
        # dummy.next = head
        # slow = dummy
        # fast = dummy
        # unlike find the middle, now you are seeing the nth from last
        # so use 2 pointer approach 
            # 1. fast one that moves n+1 place ahead
            # 2. slow which moves at nth step 
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


