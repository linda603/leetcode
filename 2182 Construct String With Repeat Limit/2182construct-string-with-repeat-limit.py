class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        heap = [(-ord(c), cnt) for c, cnt in count.items()]
        heapq.heapify(heap)

        res = ""
        while heap:
            c, cnt = heapq.heappop(heap)
            res += min(cnt, repeatLimit) * chr(-c)
            cnt = cnt - min(cnt, repeatLimit)

            while cnt > 0 and heap:
                next_c, next_cnt = heapq.heappop(heap)
                res += chr(-next_c)
                if next_cnt - 1:
                    heapq.heappush(heap, (next_c, next_cnt - 1))
                res += min(cnt, repeatLimit) * chr(-c)
                cnt = cnt - min(cnt, repeatLimit)
        return res

# Time: O(n + m + mlogm). n: len(s). m: len(heap)
# Space: O(m + n). m: len(heap), n: len(res)
