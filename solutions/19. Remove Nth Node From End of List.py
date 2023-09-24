# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # move right untill the distance between right and left = n + 1
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # move right to the end so left will be before the node that we want to remove by 1
        while right:
            right = right.next
            left = left.next

        # delete
        left.next = left.next.next

        return dummy.next
