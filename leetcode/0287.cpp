// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int i1 = 1, i2 = n, mid;
        bool bad1 = isBadVersion(i1), bad2 = false; 
        if(bad1)
            return 1;
        while(i1 < i2 - 1)
        {
            mid = i1 + (i2 - i1) / 2;
            if (isBadVersion(mid)) 
                i2 = mid;
            else
                i1 = mid;
        }
        return i2; 
    }
};
