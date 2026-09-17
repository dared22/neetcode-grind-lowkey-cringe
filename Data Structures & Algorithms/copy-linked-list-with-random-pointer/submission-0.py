"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        h1 = head

        copy_head = Node(h1.val)
        copy_tmp = copy_head

        random_copies = {
            h1: copy_head
        }
        while h1.next:
            h1 = h1.next
            new_node = Node(h1.val)
            copy_tmp.next = new_node
            copy_tmp = new_node
            
            random_copies[h1] = new_node
        original = head
        copy = copy_head

        while original:
            if original.random is not None:
                copy.random = random_copies[original.random]
            else:
                copy.random = None
            copy = copy.next
            original = original.next
            

        return copy_head