class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        queue = deque()
        res = 0

        for i in range(len(nums)):
            while queue and i > queue[0] + k - 1:
                queue.popleft()

            if (nums[i] + len(queue)) % 2 == 0:
                if i + k > len(nums):
                    return -1
                res += 1
                queue.append(i)
        
        return res

#Time: O(n)
#Space: O(n)