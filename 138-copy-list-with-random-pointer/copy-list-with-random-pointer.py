
class Solution(object):
    def copyRandomList(self, head):
        map = {}
        curr = head

        while curr:
            copy = Node(curr.val)
            map[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = map[curr]
            copy.next = map.get(curr.next)
            copy.random = map.get(curr.random)
            curr = curr.next
        return map.get(head)