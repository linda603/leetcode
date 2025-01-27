class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for cnt, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(heap, (cnt, char))
        res = ""
        
        while heap:
            cnt, char = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                cnt2, char2 = heapq.heappop(heap)
                res += char2
                if cnt2 + 1 != 0:
                    heapq.heappush(heap, (cnt2 + 1, char2))
            res += char
            if cnt + 1 != 0:
                heapq.heappush(heap, (cnt + 1, char))
        return res

# Time: O(3log3 + (a + b + c)log3) = O(a + b + c)
# Space: O(3)
