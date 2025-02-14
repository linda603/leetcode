class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> count;
        vector<int> res;

        for (int num: nums) {
            count[num]++;
        }
        for (auto& pair: count) {
            if (pair.second > n / 3) {
                res.push_back(pair.first);
            }
        }
        return res;
    }
};

// Time: O(n)
// Space: O(n)