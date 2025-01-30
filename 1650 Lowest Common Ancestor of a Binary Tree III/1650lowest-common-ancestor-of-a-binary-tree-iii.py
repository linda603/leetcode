"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        length_p = self.get_length(p)
        length_q = self.get_length(q)

        if length_p > length_q:
            diff = length_p - length_q
            while diff:
                p = p.parent
                diff -= 1
        elif length_p < length_q:
            diff = length_q - length_p
            while diff:
                q = q.parent
                diff -= 1
        
        while p != q:
            p = p.parent
            q = q.parent
        return p
    
    # get length from curr node to the root
    def get_length(self, node):
        res = 0

        while node.parent:
            node = node.parent
            res += 1
        return res

# Time: O(2h + h)
# Space: O(1)