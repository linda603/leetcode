class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        for (int i = 0; i < strs[0].size(); i++) {
            for (const string& str : strs) {
                if (i >= str.size() or strs[0][i] != str[i]) {
                    return str.substr(0, i);
                }
            }
        }
        return strs[0];
    }
};

// Time: O(n*w). w: len(shortest word)
// Space: O(w)