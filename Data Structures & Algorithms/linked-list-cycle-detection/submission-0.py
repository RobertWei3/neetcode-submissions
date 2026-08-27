# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev, temp = head, head

        while temp and temp.next:
            temp = temp.next.next
            prev = prev.next
            if temp == prev:
                return True
        return False

