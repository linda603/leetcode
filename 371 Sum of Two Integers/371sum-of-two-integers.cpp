class Solution {
public:
    int getSum(int a, int b) {
        int tmp = 0;
        
        while (b != 0) {
            tmp = a ^ b;
            b = (a & b) << 1;
            a = tmp;
        }
        return a;
    }
};

// Time: O(1) as a and b are in range [-1000, 1000]
// Space: O(1)