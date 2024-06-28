class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0

        for num in nums:
            remaining = k - num
            if remaining in freq:
                count += 1
                freq[remaining] -= 1
                if freq[remaining] == 0:
                    del freq[remaining]
            else:
                if num not in freq:
                    freq[num] = 0
                freq[num] += 1
        
        return count

#Time: O(n)
#Space: O(n)