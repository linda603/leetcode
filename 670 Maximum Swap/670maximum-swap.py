class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        n = len(arr)
        max_val_idx = n - 1
        swap_left = -1
        swap_right = n - 1

        for i in range(n - 2, -1, -1):
            # char comparision is allowed
            if arr[i] < arr[max_val_idx]:
                swap_left = i
                swap_right = max_val_idx
            elif arr[i] > arr[max_val_idx]:
                max_val_idx = i
        arr[swap_left], arr[swap_right] = arr[swap_right], arr[swap_left]
        return int("".join(arr))

# Time: O(n)
# Space: O(n)