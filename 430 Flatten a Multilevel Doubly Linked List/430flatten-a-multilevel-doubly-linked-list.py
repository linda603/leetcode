"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
    
        def dfs(prev, curr): #return tail pointer of the flattened list
                            #curr might or might not lead to the sub-list that we want to flatten
                            #prev points to the element that should precede the curr element
            if curr is None:
                return prev
            prev.next = curr
            curr.prev = prev

            tmpNext = curr.next
            tail = dfs(curr, curr.child)
            curr.child = None
            return dfs(tail, tmpNext)
        #pseudo head to make sure prev is not None
        pseudoHead = Node(None, None, head, None)
        dfs(pseudoHead, head)

        pseudoHead.next.prev = None
        return pseudoHead.next

#Time: O(n) as we visit every node in the list once
#Space: O(n) worst case, unbalance tree (tree leans to the left), dfs recursive calls up to n times