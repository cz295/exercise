class Solution {
public:
    int countOdds(int low, int high) {
        int n = (high - low) / 2;
        bool high_is_even = high % 2 == 0;
        bool low_is_even = low % 2 == 0;
        if(high_is_even && low_is_even)
            return n;
        else
            return n + 1;
    }
};
