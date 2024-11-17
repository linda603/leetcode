class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = [] # [id, start_time]

        for log in logs:
            new_log = log.split(":")
            func_id = int(new_log[0])
            call_type = new_log[1]
            curr_time = int(new_log[2])

            if call_type == "start":
                if stack:
                    prev_func_id, start_time = stack[-1]
                    res[prev_func_id] += curr_time - start_time
                stack.append([func_id, curr_time])
            else:
                prev_func_id, start_time = stack.pop()
                res[prev_func_id] += curr_time - start_time + 1
                if stack:
                    stack[-1][1] = curr_time + 1
        return res
            
# Time: O(2n). We execute the log at most 2 times.
# Space: O(n)


            
