class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1 # For first char in chars
        i = 0
        j = 1

        while j <= len(chars):
            if j < len(chars) and chars[j - 1] == chars[j]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for char in str(count):
                        chars[i] = char
                        i += 1
                count = 1 # Reset counter
            j += 1
        return i

#Time: O(n)
#Space: O(1)