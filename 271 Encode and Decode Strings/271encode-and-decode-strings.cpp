class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res;

        for (const string& word : strs) {
            res += to_string(word.size()) + "#" + word;
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        int curr_len = 0;

        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            curr_len = stoi(s.substr(i, j - i));
            res.push_back(s.substr(j + 1, curr_len));
            i = j + 1 + curr_len;
        }
        return res;  
    }
};

// Time: O(n)
// Space: O(n) due to res

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));