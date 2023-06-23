class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 2)
            return n > 0 ? true: false;
        else
        {
            if (n % 2 != 0)
                return false;
            else
                return isPowerOfTwo( n / 2);
        }
    }
};
