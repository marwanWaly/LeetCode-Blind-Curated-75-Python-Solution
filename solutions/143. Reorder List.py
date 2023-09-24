# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        hash_list = [head.val]

        curr = head.next
        while curr:
            hash_list.append(curr.val)
            curr = curr.next
        
        n = len(hash_list) - 1
        curr = head.next
        l, r = 1, n
        i = 1
        while curr:
            if i % 2 == 0:
                curr.val = hash_list[l]
                l += 1
            else:
                curr.val = hash_list[r]
                r -= 1
            i += 1
            curr = curr.next
