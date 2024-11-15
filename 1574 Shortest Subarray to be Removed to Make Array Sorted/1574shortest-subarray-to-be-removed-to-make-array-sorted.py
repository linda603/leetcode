class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # remove suffix
        l = 0
        while l < n - 1 and arr[l] <= arr[l + 1]:
            l += 1
        res = n - l - 1
        print(res, l)

        # remove prefix
        r = n - 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        res = min(res, r)
        print(res, r)

        # remove middle
        l = 0
        r = n - 1

        while l < r: # want to check l + 1 | r - 1 in the middle
            # shrink valid window
            while r < n and l + 1 < r and arr[r - 1] <= arr[r] and arr[l] <= arr[r]:
                r -= 1

            while r < n and arr[l] > arr[r]:
                r += 1
            res = min(res, r - l - 1)
            print("First mid window:", l, r, r - l - 1)

            if arr[l] > arr[l + 1]:
                break
            l += 1
        
        return res

# Time: O(3n)
# Space: O(1)