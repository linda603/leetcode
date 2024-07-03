class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head = []
        tail = []
        l = 0
        r = len(costs) - 1
        res  = 0

        while k > 0:
            while len(head) < candidates and l <= r: #O(mlogm)
                heapq.heappush(head, costs[l])
                l += 1
            while len(tail) < candidates and l <= r: #O(mlogm)
                heapq.heappush(tail, costs[r])
                r -= 1
            
            minHead = head[0] if head else float("inf")
            minTail = tail[0] if tail else float("inf")

            if minHead <= minTail:
                res += minHead
                heapq.heappop(head) #O(logm) time
            else:
                res += minTail
                heapq.heappop(tail)
            k -= 1
        return res

#Time: O((k + m)logm) m: candidates
#Space: O(2m)