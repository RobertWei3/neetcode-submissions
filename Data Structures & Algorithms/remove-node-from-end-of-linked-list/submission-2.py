# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        for _ in range(n):
            # prev = curr
            curr = curr.next

        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

        return dummy.next

        
        