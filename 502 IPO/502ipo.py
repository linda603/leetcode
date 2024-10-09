class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_capitals_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capitals_heap)
        max_profits_heap = []

        for cnt in range(k):
            while min_capitals_heap and min_capitals_heap[0][0] <= w:
                c, p = heapq.heappop(min_capitals_heap)
                heapq.heappush(max_profits_heap, -p)
            
            # if no capital <= w, return w
            if not max_profits_heap: return w
            w += abs(heapq.heappop(max_profits_heap))
        return w

#Time: O(n + n + klogn)
#Space: O(n)