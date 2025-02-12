class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen; // val -> index

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (seen.count(diff) && seen[diff] != i) {
                return {i, seen[diff]};
            }

            seen[nums[i]] = i;
        }
        return {};
    }
};

// Time: O(n)
// Space: O(n)