class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        max_queue = collections.deque() # monotonic decreasing queue
        min_queue = collections.deque() # monotonic increasing queue

        l = 0
        for r in range(len(nums)):
            while max_queue and nums[max_queue[-1]] <= nums[r]:
                max_queue.pop()
            while min_queue and nums[min_queue[-1]] >= nums[r]:
                min_queue.pop()
            max_queue.append(r)
            min_queue.append(r)

            while nums[max_queue[0]] - nums[min_queue[0]] > 2:
                l += 1
                if max_queue[0] < l:
                    max_queue.popleft()
                if min_queue[0] < l:
                    min_queue.popleft()
            res += r - l + 1
        return res

# Time: O(n)
# Space: O(n)