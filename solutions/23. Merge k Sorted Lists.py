# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while True:
            smallest = (-1, None)
            for i, lis in enumerate(lists):
                if (lis and smallest[0] == -1) or (lis and lis.val < smallest[1].val):
                    smallest = (i, lis)

            if smallest[0] == -1:
                break
            curr.next = smallest[1]
            lists[smallest[0]] = lists[smallest[0]].next
            curr = curr.next
        
        return dummy.next
