# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Get 1st half and 2nd half lists
        mid = self.get_mid_node(head)
        second = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(second)
        return self.merge(left, right)
    
    def get_mid_node(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

# Time: O(nlogn + nlogn) = O(nlogn). O(n) to find mid pointer.
#                                   O(logn) for recursive calls to split 2 halves
#                                   O(nlogn) to merge 2 lists
# Space: O(logn). dfs() recursive calls take O(logn). O(1) to build new list while merging, only use extra dummy node for merge() API.