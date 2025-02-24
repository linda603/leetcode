class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int res = 0;

        for (int num: numSet) {
            if (numSet.find(num - 1) == numSet.end()) {
                int curr_len = 1;
                while (numSet.find(num + 1) != numSet.end()) {
                    curr_len += 1;
                    num++;
                }
                res = max(res, curr_len);
            }
        }
        return res;
    }
};

// Time: O(n + n)
// Space: O(n)