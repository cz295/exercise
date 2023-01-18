class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if(intervals.size() <= 1)
            return (int) intervals.size();
        sort(
            intervals.begin(), intervals.end(),
            [](const vector<int> & a, const vector<int> & b) -> bool
            { 
                if(a[0] != b[0])
                    return a[0] < b[0]; 
                else
                    return a[1] < b[1];
            }
        );
        priority_queue <int, vector<int>, greater<int>> curr_meeting;
        int max_overlap = 1;
        for(auto i = 0; i <= intervals.size() - 1; ++i)
        {
            while(!curr_meeting.empty() && intervals[i][0] >= curr_meeting.top())
                curr_meeting.pop();
            curr_meeting.push(intervals[i][1]);
            if(curr_meeting.size() > max_overlap)
                  max_overlap = curr_meeting.size();
        }
        return max_overlap;
    }
};
