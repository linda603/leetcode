class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-cnt, c) for c, cnt in count.items()]
        heapq.heapify(heap)
        prev_hold = None
        res = ""

        while heap:
            cnt, c = heapq.heappop(heap)
            res += c
            if prev_hold:
                heapq.heappush(heap, prev_hold)
                prev_hold = None
            if cnt + 1 != 0:
                prev_hold = (cnt + 1, c)
        return "" if prev_hold else res

# Time: O(n + 26 + 26log26 + nlog26) = O(n)
# Space: O(26) = O(1)