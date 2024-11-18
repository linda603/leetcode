class Solution {
private:
    bool is_digit(char c) {
        return c >= '0' && c <= '9';
    }

public:
    int myAtoi(string s) {
        int n = s.size();
        if (n == 0) return 0;

        int i = 0;
        while (i < n and s[i] == ' ') i++;

        if (i == n) return 0;

        // to handle sign cases
        bool is_negative = false;

        if (s[i] == '+') {
            i++;
        }
        else if (s[i] == '-') {
            i++;
            is_negative = true;
        }

        int res = 0;
        while (i < n && is_digit(s[i])) {
            int digit = s[i] - '0';

            // handle overflow res
            if ((res > INT_MAX / 10) || ((res == INT_MAX / 10) && digit > 7)) {
                return is_negative ? INT_MIN : INT_MAX;
            }

            res = res * 10 + digit;
            i++;
        }
        return is_negative ? -res : res;
    }
};

// Time: O(n)
// Space: O(1)
