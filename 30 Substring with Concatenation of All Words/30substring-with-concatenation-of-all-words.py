class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = {}
        for word in words:
            count[word] = 1 + count.get(word, 0)

        res = []
        n = len(s)
        m = len(words)
        w = len(words[0])

        for p in range(w):
            left, i = p, p
            seen = {}
            curr = 0
            while i < n - w + 1:
                tmp = s[i: i+w]
                if tmp not in count:
                    seen = {}
                    curr = 0
                    left = i + w
                else:
                    seen[tmp] = 1 + seen.get(tmp, 0)
                    curr += 1
                    while seen[tmp] > count[tmp]:
                        seen[s[left: left+w]] -= 1
                        curr -= 1
                        left += w
                if curr == m:
                    res.append(left)
                    seen[s[left: left+w]] -= 1
                    curr -= 1
                    left += w
                i += w
        return res

#Time: O(w*n)
#Space: O(m*w)