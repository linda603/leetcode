"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        queue = collections.deque()
        if root:
            queue.append(root)
        
        while queue:
            qLen = len(queue)
            newLevel = []
            for i in range(qLen):
                node = queue.popleft()
                newLevel.append(node.val)
                if node.children:
                    queue.extend(node.children)
            res.append(newLevel)
        return res

#Time: O(n)
#Space: O(n)