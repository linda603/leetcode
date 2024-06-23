# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        
        def dfs(lowerBound, upperBound):
            nonlocal i
            if i == len(preorder):
                return None
            if preorder[i] < lowerBound or preorder[i] > upperBound:
                return None
            currVal = preorder[i]
            root = TreeNode(preorder[i])
            i += 1
            root.left = dfs(lowerBound, currVal)
            root.right = dfs(currVal, upperBound)
            return root
        
        return dfs(float("-inf"), float("inf"))

#Time: O(n)
#Space: O(h)