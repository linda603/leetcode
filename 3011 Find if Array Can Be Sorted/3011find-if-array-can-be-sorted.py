class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits = {}
        bits = self.get_bits(nums)
        
        prev_max = float("-inf")
        curr_min = nums[0]
        curr_max = nums[0]

        for num in nums:
            if bits[num] == bits[curr_min]:
                curr_min = min(curr_min, num)
                curr_max = max(curr_max, num)
            else: # reached the new group
                if curr_min < prev_max:
                    return False
                prev_max = curr_max
                curr_min = num
                curr_max = num
                
        if curr_min < prev_max:
            return False

        return True
    
    def get_bits(self, nums):
        bits = {}

        for num in nums:
            if num == 0:
                bits[0] = 0
                continue
            res = 0
            val = num

            while val > 0:
                res += val % 2
                val = val // 2
            bits[num] = res
        return bits

# Time: O(n). get_bits is O(1) as 1 <= nums[i] <= 2^8
# Space: O(1)