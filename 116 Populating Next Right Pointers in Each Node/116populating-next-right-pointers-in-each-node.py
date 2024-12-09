"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root
        nxt = curr.left if curr else None

        while curr and nxt: # Ensure 2 levels are available, so can process the logics
            curr.left.next = curr.right
            if curr.next and curr.right:
                curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root

# Time: O(n)
# Space: O(1)