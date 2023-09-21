# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while s:
            if s.next is None or f.next is None:
                return False
            
            if f.next.next is None:
                return False

            s = s.next
            f = f.next.next

            if s == f:
                return True
            
        return False
