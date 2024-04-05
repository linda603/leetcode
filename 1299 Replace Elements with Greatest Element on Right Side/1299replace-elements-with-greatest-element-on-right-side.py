class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        for i in range(len(arr) - 1):
            maxVal = float("-inf")
            for j in range(i + 1, len(arr)):
                maxVal = max(maxVal, arr[j])
            arr[i] = maxVal
        arr[len(arr) - 1] = -1
        return arr
    
#Time: O(n^2)
#Space: O(1)
"""
        maxValR = -1

        for i in range(len(arr) - 1, -1 , -1):
            newMax = max(arr[i], maxValR)
            arr[i] = maxValR
            maxValR = newMax
        return arr

#Time: O(n)
#Space: O(1)
