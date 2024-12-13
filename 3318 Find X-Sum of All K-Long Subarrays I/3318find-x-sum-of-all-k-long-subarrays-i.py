class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        total = 0
        count = {}

        l = 0
        for r in range(len(nums)):
            count[nums[r]] = 1 + count.get(nums[r], 0)
            if r - l + 1 == k:
                curr_sum = self.sum_x_freq(count, x, k)
                res.append(curr_sum)
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
        return res
    
    def sum_x_freq(self, count, x, k):
        freq = [[] for _ in range(k + 1)]
        res = 0

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            lists = freq[i]
            lists.sort()
            while lists:
                res += lists.pop() * i
                x -= 1
                if x == 0:
                    return res
        return res # case x < len(count)

# Time: O(n * (klogk)). O(klogk) for sum_x_freq().
# Space: O(k + k) = O(k). O(k) for count. O(k) for freq