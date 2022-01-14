class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        last_index = dict()
        last_index[s[0]] = 0
        max_len = 1
        start_i = 0
        for end_i in range(1, len(s)):
            if s[end_i] in last_index and last_index[s[end_i]] >= start_i:
                max_len = max(max_len, end_i - start_i)
                start_i = last_index[s[end_i]] + 1
                last_index[s[end_i]] = end_i
            else:
                last_index[s[end_i]] = end_i
        return max(max_len, end_i - start_i + 1)

    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0;
        l = 0;
        seenChars = {};
        for r, c in enumerate(s):
            if c in seenChars and seenChars[c] >= l:
                l = seenChars[c] + 1;
            elif maxLen < r - l + 1:
                maxLen = r - l + 1;
            seenChars[c] = r;
        return maxLen;
