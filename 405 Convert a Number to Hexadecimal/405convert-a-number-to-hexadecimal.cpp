class Solution {
public:
    string toHex(int num) {
        if (num == 0) return "0";
        string int_to_hex = "0123456789abcdef";
        string res;
        int count = 0;

        while (num && count < 8) {
            res = int_to_hex[(num & 15)] + res;
            num >>= 4;
            count++;
        }
        return res;
    }
};

// Time: O(32)
// Space: O(1)