# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        reversed_head = prev
        if n == 1:
            reversed_head = reversed_head.next
        else:
            node = reversed_head
            counter = 1

            while counter < n - 1:
                node = node.next
                counter += 1

            node.next = node.next.next

        node = reversed_head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        
        return prev


