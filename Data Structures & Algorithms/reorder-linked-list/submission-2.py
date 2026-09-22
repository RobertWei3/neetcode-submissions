# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second list 
        # split into two list
        second = slow.next
        before = slow.next = None
        # after = second.next
        while second:
            after = second.next
            second.next = before
            before = second
            second = after
        

        # merge two list
        first, second = head, before
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2












        