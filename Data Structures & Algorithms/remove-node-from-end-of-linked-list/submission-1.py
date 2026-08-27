# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # first: reverse the list
        # first, prev = head, None
        # while first:
        #     temp = first.next
        #     first.next = prev
        #     prev = first
        #     first = temp

        # # remove the item at the nth postion from the reverse list
        # if n == 1:
        #     prev = prev.next
        # else:
        #     curr = prev
        #     for _ in range(n - 2):
        #         curr = curr.next
            
        #     curr.next = curr.next.next
            
        # second, new_head = prev, None
        # while second:
        #     temp = second.next
        #     second.next = new_head
        #     new_head = second
        #     second = temp
        # return new_head
        
        # only iterate once
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next

        # delete 
        left.next = left.next.next

        return dummy.next


        
        