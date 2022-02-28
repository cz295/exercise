class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_index = {}
        last_index = {}
        for i, a in enumerate(s):
            if a not in first_index:
                first_index[a] = i
                last_index[a] = i
            else:
                last_index[a] = i
        index_locs = [
            [first_index[a], last_index[a]] for a in first_index
        ]
        index_locs.sort(key=lambda x: (x[0], x[1]))
        # print(index_locs)
        prev = index_locs[0][1]
        cut_index = []
        for a in index_locs[1:]:
            if a[0] > prev:
                prev = a[1]
                cut_index.append(a[0])
            else:
                prev = max(prev, a[1])
            # print(cut_index)
        ret_index = []
        prev = 0
        for x in cut_index:
            ret_index.append(x - prev)
            prev = x
        ret_index.append(len(s) - prev)
        return ret_index
        
