class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        count_zero = 0 # "0" in the left partition
        count_one = 0 # "1" in the right partition

        for c in s:
            if c == "1":
                count_one += 1
        
        for i in range(len(s) - 1):
            c = s[i]
            if c == "0":
                count_zero += 1
            elif c == "1":
                count_one -= 1
            curr_score = count_zero + count_one
            res = max(res, curr_score)
        return res

# Time: O(2n)
# Space: O(1)