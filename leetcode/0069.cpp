class Solution {
public:
    int mySqrt(int x) {
        if(x <= 1) 
            return x;
        int lower = 1, upper = int(x / 2) + 1;
        while(lower < upper - 1)
        {
            long mid = lower + int((upper - lower) / 2);
            long prod = mid * mid;
            if(prod == x)
                return mid;
            else if (prod > x)
                upper = mid;
            else
                lower = mid;
        }
        return lower;
    }
};
