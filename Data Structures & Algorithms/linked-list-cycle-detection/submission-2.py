# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_head = head
        seen_set = set()
        while list_head:
            if list_head in seen_set:
                return True
            else:
                seen_set.add(list_head)
                list_head = list_head.next
        return False
    