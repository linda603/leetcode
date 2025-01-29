class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = [(-cnt, c) for c, cnt in count.items()]
        heapq.heapify(heap)
        res = ""

        while heap:
            cnt, c = heapq.heappop(heap)
            res += -cnt * c
        return res

# Time: O(n + 26 + 26log26 + 26log26) = O(n)
# Space: O(26 + 26) = O(1)