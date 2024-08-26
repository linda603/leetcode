# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = {}
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                return "N"
            string = [str(node.val), dfs(node.left), dfs(node.right)]
            string = ",".join(string)

            if string in subtrees and len(subtrees[string]) == 1:
                res.append(node)

            if string not in subtrees:
                subtrees[string] = []
            subtrees[string].append(node)
            return string
        
        dfs(root)
        return res

#Time: O(n^2). To travese all subtrees O(n^2) time.
#Space: O(n^2) keys in subtrees hash map is O(n^2) space.