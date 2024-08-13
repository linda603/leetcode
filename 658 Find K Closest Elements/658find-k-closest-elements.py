class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = [0, k - 1]
        total = 0

        for i in range(k):
            total += abs(arr[i] - x)
        
        for i in range(k, len(arr)):
            curr = total + abs(arr[i] - x) - abs(arr[i - k] - x)
            if curr < total:
                res = [i - k + 1, i]
        
        l, r = res
        return arr[l: r + 1]

#Time: O(n)
#Space: O(1)