# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Brute force
        lists = []
        curr = head

        while curr:
            lists.append(curr.val)
            curr = curr.next
        return self.is_pal(lists)
    
    def is_pal(self, lists):
        l = 0
        r = len(lists) - 1

        while l < r:
            if lists[l] != lists[r]:
                return False
            l += 1
            r -= 1
        return True

# Time: O(2n)
# Space: O(n)