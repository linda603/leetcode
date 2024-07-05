# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head.next
        prev = head

        prevPoint = 0
        firstPoint = 0
        i = 1

        minDis = float("inf")
        maxDis = float("-inf")

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
                (curr.val < prev.val and curr.val < curr.next.val):
                if firstPoint:
                    print("minDis:", minDis)
                    print("i, prevPoint:", i, prevPoint)
                    maxDis = i - firstPoint
                    minDis = min(minDis, i - prevPoint)
                else:
                    firstPoint = i
                prevPoint = i
            i += 1
            prev = curr
            curr = curr.next

        return [-1, -1] if minDis == float("inf") else [minDis, maxDis]

#Time: O(n)
#Space: O(1)