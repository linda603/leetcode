class Solution {
public:
    long long minEnd(int n, int x) {
        long long res = x;

        for (int i = 1; i < n; i ++) {
            res ++;
            res = res | x;
        }
        return res;
    }
};

// Time: O(n)
// Space: O(1)