class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = [0] * 26
        temp = [0] * 26
        res = []

        for word in words2:
            for c in word:
                temp[ord(c) - ord("a")] += 1
            for i in range(26):
                count[i] = max(count[i], temp[i])
            temp = [0] * 26
        
        for word in words1:
            for c in word:
                temp[ord(c) - ord("a")] += 1
            flag = True
            for i in range(26):
                if temp[i] < count[i]:
                    flag = False
                    break
            if flag:
                res.append(word)
            temp = [0] * 26
        return res

# Time: O(ml + nl). m: len(words2), n: len(words1)
# Space: O(26 + 26 + n) = O(n) due to res