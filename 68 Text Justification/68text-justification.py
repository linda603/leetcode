class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr_line = []
        curr_len = 0

        for word in words:
            # case: not able to put word to curr line
            if len(curr_line) + curr_len + len(word) > maxWidth:
                total_spaces = maxWidth - curr_len
                if len(curr_line) == 1:
                    curr_line[0] += " " * total_spaces
                    res.append(curr_line[0])
                else:
                    spaces_per_word = total_spaces // (len(curr_line) - 1)
                    remain = total_spaces % (len(curr_line) - 1)

                    for i in range(len(curr_line) - 1):
                        curr_line[i] += spaces_per_word * " "
                        if remain:
                            curr_line[i] += " "
                            remain -= 1
                    res.append("".join(curr_line))
                curr_line = []
                curr_len = 0
            curr_line.append(word)
            curr_len += len(word)
        
        # handle last line
        last_line = " ".join(curr_line)
        remain = maxWidth - len(last_line)
        last_line += remain * " "
        res.append(last_line)
        return res

# Time: O(nl). n: len(words), l: len(average word)
# Space: O(nl + m). res: O(nl), curr_line: O(maxWidth)