class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        queue = collections.deque()

        while heap or queue:
            time += 1
            if heap:
                cnt = heapq.heappop(heap)
                if cnt + 1 != 0:
                    queue.append((time + n, cnt + 1))
            while queue and queue[0][0] == time:
                heapq.heappush(heap, queue.popleft()[1])
        return time 

# Time: O(n + 26 + 26log26 + 26log26) = O(n)
# Space: O(26 + 26)
