class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack1 = [] # monotonic increasing stack to keep track of next smaller element
        nxt_smaller = [n] * n
        stack2 = [] # monotonic increasing stack to keep track of previous smaller element
        prev_smaller_equal = [-1] * n
        mod = 10 ** 9 + 7

        for i in range(n):
            while stack1 and arr[stack1[-1]] > arr[i]:
                nxt_smaller[stack1.pop()] = i
            stack1.append(i)

        for i in range(n - 1, -1, -1):
            while stack2 and arr[stack2[-1]] >= arr[i]:
                prev_smaller_equal[stack2.pop()] = i
            stack2.append(i)
        
        total = 0
        for i, num in enumerate(arr):
            right = nxt_smaller[i] - i
            left = i - prev_smaller_equal[i]
            total = (total + num * left * right) % mod
        return total

# Time: O(3n)
# Space: O(n)