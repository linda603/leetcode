class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        start_arr = list(start)
        result_arr = list(result)
        i = 0

        # XXXXXL - LXXXXX
        # n^2
        for i in range(len(start_arr)):
            if start_arr[i] != result_arr[i]:
                j = i
                while j + 1 < len(start_arr) and start_arr[j] == start_arr[j + 1]:
                    j += 1
                if "".join(start_arr[j: j + 2]) not in ["XL", "RX"] or j + 1 == len(start_arr):
                    return False
                self.swap(start_arr, i, j + 1)
        return True
    
    def swap(self, string, i, j):
        string[i], string[j] = string[j], string[i]

# Time: O(n^2)
# Space: O(n)