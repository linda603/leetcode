class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []

        i = 0
        while i < len(s):
            curr_len = 0
            while s[i] != '#':
                curr_len = curr_len * 10 + int(s[i])
                i += 1
            res.append(s[i + 1: i + 1 + curr_len])
            i = i + 1 + curr_len
        return res        


# Time: O(n) for encode() and decode()
# Space: O(n) due to res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))