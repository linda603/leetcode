# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = {0: 1} #presfixSum of each node from root
        res = 0

        def dfs(node, curr):
            nonlocal res
            if not node:
                return
            # Calculate current path sum
            curr += node.val
            #calculate previous path sum
            prev = curr - targetSum
            res += cache.get(prev, 0)

            # Update curr path sum in cache
            cache[curr] = cache.get(curr, 0) + 1

            # dfs calls
            dfs(node.left, curr)
            dfs(node.right, curr)
            
            # When move to a different branch, curr path sum is not available anymore.
            # Remove/reduce curr sum from cache
            cache[curr] -= 1
            return
        
        dfs(root, 0)
        return res

#Time: O(n)
#Space: O(h)