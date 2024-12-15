class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque() # monotonic decreasing queue

        l = 0
        for r in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            queue.append(r)

            if queue[0] < l:
                queue.popleft()

            if r - l + 1 == k:
                res.append(nums[queue[0]])
                l += 1
        return res

# Time: O(n)
# Space: O(2n)