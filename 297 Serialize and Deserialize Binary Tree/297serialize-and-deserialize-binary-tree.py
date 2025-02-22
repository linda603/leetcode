# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.idx = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ",".join(self.dfs1(root))        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")

        self.idx = 0
        return self.dfs2(arr)

    def dfs1(self, node):
        if not node:
            return ["N"]
        left = self.dfs1(node.left)
        right = self.dfs1(node.right)
        return [str(node.val)] + left + right
    
    def dfs2(self, data):
        if data[self.idx] == "N":
            self.idx += 1
            return None
        root = TreeNode(data[self.idx])
        self.idx += 1
        root.left = self.dfs2(data)
        root.right = self.dfs2(data)
        return root

# Time: O(n)
# Space: O(n)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))