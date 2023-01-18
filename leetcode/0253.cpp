// ref answer


// const size_t Start = 0;
// const size_t End = 1;

// class Solution {
// public:
//     int minMeetingRooms(vector<vector<int>>& intervals) {
//         const int len = intervals.size();
//         int requiredRooms = 0;
//         int curRooms = 0;
//         vector<int> futureEnds; make_heap(futureEnds.begin(), futureEnds.end(), std::greater<>{});

//         std::sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) -> bool {
//             return a[Start] < b[Start] || (a[Start] == b[Start] && a[End] < b[End]);
//         });

//         for (size_t i = 0; i < len; i++) {
//             vector<int>& cur = intervals[i];

//             while (futureEnds.size() && futureEnds.front() <= cur[Start]) {
//                 curRooms--;
//                 pop_heap(futureEnds.begin(), futureEnds.end(), std::greater<>{}); futureEnds.pop_back();
//             }

//             curRooms++;
//             futureEnds.push_back(cur[End]); push_heap(futureEnds.begin(), futureEnds.end(), std::greater<>{});
//             requiredRooms = std::max(requiredRooms, curRooms);
//         }

//         return requiredRooms;
//     }
// };
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
