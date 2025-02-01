class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        for (start, target), rate in zip(pairs1, rates1):
            adj1[start].append((target, rate))
            adj1[target].append((start, 1 / rate))
        
        for (start, target), rate in zip(pairs2, rates2):
            adj2[start].append((target, rate))
            adj2[target].append((start, 1 / rate))

        def dfs(node, curr, day, prev):
            if day > 2:
                return 0
            res = 0
            if day == 1:
                if node not in adj1:
                    return max(0, dfs(node, curr, day + 1))
                for nei, rate in adj1[node]:
                    if nei == prev:
                        continue
                    if nei == initialCurrency:
                        return curr * rate
                    curr_day = dfs(nei, curr * rate, day, node)
                    next_day = dfs(nei, curr * rate, day + 1, None)
                    print(curr_day, next_day)
                    res = max(res, curr_day, next_day)
            else:
                if node not in adj2:
                    return 0
                if node == initialCurrency:
                    return 1
                for nei, rate in adj2[node]:
                    print("here")
                    if nei == prev:
                        continue
                    if nei == initialCurrency:
                        print(curr * rate)
                        return curr * rate
                    curr_day = dfs(nei, curr * rate, day, node)
                    next_day = dfs(nei, curr * rate, day + 1, None)
                    print(curr_day, nei, curr * rate, day, node)
                    res = max(res, curr_day, next_day)
            return res
        return max(1.0, dfs(initialCurrency, 1.0, 1, None))