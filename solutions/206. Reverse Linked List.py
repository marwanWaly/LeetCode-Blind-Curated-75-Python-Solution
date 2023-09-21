# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_head = None
        while head:
            last_head = ListNode(val=head.val, next=last_head)
            head = head.next
        return last_head
