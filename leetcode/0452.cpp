class Solution {
public:
    static bool comp(vector <int>& a,vector <int>& b)
    {
        return(a[1] < b[1]);
    }


    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), comp);
        int max_x = points[0][1], res = 1;
        for(int i = 1; i < points.size(); ++ i)
        {
            if(points[i][0] > max_x)
            {
                max_x = points[i][1];
                res += 1;
            }
        }
        return res;
    }
};
