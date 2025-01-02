class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for i in range(len(nums)):
            if not seq or seq[-1] < nums[i]:
                seq.append(nums[i])
            else:
                replace_i = self.upper_bound(seq, nums[i])
                seq[replace_i] = nums[i]
        return len(seq)
    
    def upper_bound(self, seq, val):
        l = 0
        r = len(seq) - 1
        res = r

        while l <= r:
            mid = (l + r) // 2
            if seq[mid] == val:
                return mid
            elif seq[mid] > val:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Time: O(nlogn)
# Space: O(n)