# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1, l2 = head, head.next
        
        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next

        second = l1.next
        l1.next = None
        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1 ,tmp2


        
            

            
            
