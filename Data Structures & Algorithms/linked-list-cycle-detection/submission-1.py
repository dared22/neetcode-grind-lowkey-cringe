# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_head = head
        seen_list = []
        while list_head:
            if list_head in seen_list:
                return True
            else:
                seen_list.append(list_head)
                list_head = list_head.next
        return False
    