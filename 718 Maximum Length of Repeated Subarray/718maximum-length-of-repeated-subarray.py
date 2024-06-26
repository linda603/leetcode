class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #dp[i][j] means the length of repeated array of nums1[i:] and nums2[j:]
        dp = [[0 for j in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        res = 0

        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                #If both characters are the same, we add 1 diagonally, which is 1 + dp[i + 1][j + 1]
                #In other word, we extend the repeated subarray by 1
                #E.g. a    [2], b =    [2] length of repeated array is 1
                #     a [1, 2], b = [1, 2] length of repeated array is 2
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    res = max(res, dp[i][j])
                #else:
                #If we are looking for longest common sequence,
                #Then dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                #However, this problem is looking for subarray,
                #Since both character is not equal, which means we need to break it here
                #Hence set dp[i][j] = 0
        
        return res

#Time: O(m*n)
#Space: O(m*n)