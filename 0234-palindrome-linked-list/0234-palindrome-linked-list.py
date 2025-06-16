# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # Find Middle then reverse and then check
        # Middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse
        prev = None

        while slow != None:
            nextPtr = slow.next
            slow.next = prev

            #update
            prev = slow
            slow = nextPtr
        
        # Check
        left = head
        right = prev

        while right!= None:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        return True
        