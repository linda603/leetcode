class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        queue = deque()

        time = 0
        while heap or queue:
            if heap:
                count = heapq.heappop(heap)
                if count + 1 != 0: # still need to process this task later after time + n
                    queue.append((count + 1, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
            time += 1
        return time

# Time: O(n + 26 + 26log26) = O(n)
# Space: O(26 + 26) = O(1)