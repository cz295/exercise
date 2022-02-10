class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int cnt = 0, idx = 0;
        while(idx <= flowerbed.size() - 1){
            int prev = idx == 0? 0 : flowerbed[idx - 1];
            int next = idx == flowerbed.size() - 1 ? idx : idx + 1;
            if (prev == 0 && flowerbed[idx] == 0 && flowerbed[next] == 0)
            {
                cnt += 1;
                idx += 2;
            }
            else
            {
                idx += 1;
            }
            if (cnt >= n)
                return true;
        }
        return false;
    }
};
