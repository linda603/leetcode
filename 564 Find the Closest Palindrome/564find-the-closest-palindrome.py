class Solution:
    def nearestPalindromic(self, n: str) -> str:
        string = list(n)
        total_len = len(string)
        is_odd = total_len % 2
        half = total_len // 2 + 1 if is_odd else total_len // 2
        all_pos = [0] * 5

        all_pos[0] = self.get_pal(int("".join(string[:half])) - 1, is_odd)
        all_pos[1] = self.get_pal(int("".join(string[:half])), is_odd)
        all_pos[2] = self.get_pal(int("".join(string[:half])) + 1, is_odd)
        all_pos[3] = 10 ** (total_len - 1) - 1
        all_pos[4] = 10 ** total_len + 1
        #print(all_pos)

        res = float("inf")
        min_diff = float("inf")
        for num in all_pos:
            if num == int(n):
                continue
            curr_diff = abs(num - int(n))
            if curr_diff < min_diff:
                res = num
                min_diff = curr_diff
            elif curr_diff == min_diff and num < res:
                res = num
        return str(res)
    
    def get_pal(self, num, is_odd):
        string = list(str(num))

        if is_odd:
            return int("".join(string + string[:-1][::-1]))
        else:
            return int("".join(string + string[::-1]))
    
# Time: O(log10(n))
# Space: O(log10(n)) due to build string[:half]