class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i):
        p = self.par[i]

        while p != self.par[p]:
            p = self.par[self.par[p]]
            p = self.par[p]
        return p
        
    def union(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)

        if par_a == par_b:
            return False
        if self.rank[par_a] >= self.rank[par_b]:
            self.rank[par_a] += self.rank[par_b]
            self.par[par_b] = par_a
        else:
            self.rank[par_b] += self.rank[par_a]
            self.par[par_a] = par_b
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind(len(accounts))
        email_to_idx = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in email_to_idx:
                    email_to_idx[email] = i
                else:
                    union_find.union(email_to_idx[email], i) # merge 2 nodes indexes together if they share the same email
        
        idx_to_emails = {}
        for email, idx in email_to_idx.items():
            parent_idx = union_find.find(idx)
            if parent_idx not in idx_to_emails:
                idx_to_emails[parent_idx] = []
            idx_to_emails[parent_idx].append(email)
        
        res = []
        for idx, emails in idx_to_emails.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails))
        return res

# Time: O(nl*n + nl + nllogl). n: len(accounts), l: longest list of an account
# Space: O(nl)


