# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        def convert_to_lists(head):
            if not head:
                return
            res = []
            while head:
                res.append(head.val)
                head = head.next
            return res

        def convert_to_tree(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(lists[mid])
            root.left = convert_to_tree(l, mid - 1)
            root.right = convert_to_tree(mid + 1, r)
            return root
        
        lists = convert_to_lists(head)
        return convert_to_tree(0, len(lists) - 1)
    
# Time: O(n + n). O(n) to build the sorted lists. O(n) to build the new tree
# Space: O(n + logn + n). O(n) due to sorted lists. O(logn) due to dfs() depth. O(n) for the new tree