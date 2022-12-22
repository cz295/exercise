class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        else:
            i_s = i_t = 0
            while i_t < len(t):
                if s[i_s] == t[i_t]:
                    i_s += 1
                    i_t += 1
                else:
                    i_t += 1
                if i_s == len(s):
                    return True
            return False
                
