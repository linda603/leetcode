# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = self.get_length(head)

        base_len = length // k
        extra_nodes = length % k
        curr = head
        res = []

        for i in range(k):
            res.append(curr)
            curr_len = base_len + 1 if extra_nodes else base_len
            for j in range(curr_len - 1): # 1 -> 2 -> 3, 3 nodes, we just need to traverse 2 times
                if not curr:
                    break
                curr = curr.next
            extra_nodes -= 1 if extra_nodes > 0 else 0
            if curr:
                tmp = curr.next
                curr.next = None
                curr = tmp

        return res

    def get_length(self, head):
        res = 0
        curr = head

        while curr:
            res += 1
            curr = curr.next
        return res

# Time: O(max(n, k))
# Space: O(k) due to res, no new nodes is created