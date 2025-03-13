class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index_map = {}
        count = 0

        for i, c in enumerate(s):
            if c not in index_map:
                index_map[c] = []
            index_map[c].append(i)
        
        for word in words:
            curr_idx = -1
            for i, c in enumerate(word):
                if c not in index_map:
                    break
                curr_idx = self.binary_search(index_map[c], curr_idx)
                if curr_idx == -1:
                    break
                if i == len(word) - 1:
                    count += 1
        return count
    
    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                res = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        return res

# Time: O(m + nllogm)
# Space: O(26) = O(1)