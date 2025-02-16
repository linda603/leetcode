class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;

        for (const auto& word: strs) {
            vector<int> count(26, 0);
            for (char c: word) {
                count[c - 'a']++;
            }
            string key = convert_to_string(count);
            anagrams[key].push_back(word);
        }

        vector<vector<string>> res;
        for (auto& pair: anagrams) {
            res.push_back(pair.second);
        }
        return res;
    }

    string convert_to_string(vector<int>& count) {
        string res = to_string(count[0]);

        for (int i = 1; i < 26; i++) {
            res += ',' + to_string(count[i]);
        }
        return res;
    }
};

// Time: O(nw*(26 + 26))
// Space: O(nw)