class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t if t in s else ""

        def check_matched(dict_ref, dict_test):
            for i in dict_ref:
                if dict_test[i] < dict_ref[i]:
                    return False
            return True

        from collections import defaultdict, deque
        t_dict = defaultdict(int)
        for _t in t:
            t_dict[_t] += 1    

        sliding_letter_dict = defaultdict(int)
        string_idx = deque()
        start_idx = 0
        min_str = ""
        min_length = len(s)
        for i, x in enumerate(s):
            if x in t_dict:
                if len(string_idx) == 0:
                    start_idx = i
                sliding_letter_dict[x] += 1
                string_idx.append(i)            
                while check_matched(t_dict, sliding_letter_dict):
                    _len = i - start_idx + 1
                    if _len <= min_length:
                        min_length = _len
                        min_str = s[start_idx:i+1]
                    start_idx = string_idx.popleft()
                    sliding_letter_dict[s[start_idx]] -= 1
                    start_idx = string_idx[0]
        return min_str

        
