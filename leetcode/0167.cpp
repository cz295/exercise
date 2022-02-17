class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int p1 = 0, p2 = numbers.size() - 1;
        int curr_sum = numbers[p1] + numbers[p2];
        while(curr_sum != target)
        {
            if(target > curr_sum)
                p1 += 1;
            else
                p2 -= 1;
            curr_sum = numbers[p1] + numbers[p2];
        }
        return {p1 + 1, p2+1};
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1, sum;
        while(l < r){
            sum = numbers[l] + numbers[r];
            if (sum == target) break;
            if (sum < target) ++l;
            else --r;
        }
        return {l+1, r+1};
    }
};
