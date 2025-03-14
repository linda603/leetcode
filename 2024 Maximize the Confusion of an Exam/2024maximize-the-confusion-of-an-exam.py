class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        count_t = 0
        count_f = 0
        l = 0

        for r in range(len(answerKey)):
            if answerKey[r] == "T":
                count_t += 1
            else:
                count_f += 1
            while count_t > k and count_f > k:
                if answerKey[l] == "T":
                    count_t -= 1
                else:
                    count_f -= 1
                l += 1
            if r - l + 1 - max(count_t, count_f) <= k:
                res = max(res, r - l + 1)
        return res