class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}

        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        heap = [(-cnt, c) for c, cnt in count.items()]
        heapq.heapify(heap)

        res = ""
        prev = None
        while heap:
            cnt, c = heapq.heappop(heap)
            res += c
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if cnt + 1 != 0:
                prev = (cnt + 1, c)
        return res if not prev else ""

# Time: O(n + 26 + 26log26 + nlog26) = O(1)
# Space: O(26 + 26) = O(1)
            