class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        for a, b in zip(s, t):
            if a not in mapping_s_to_t:
                if b not in mapping_t_to_s:
                    mapping_s_to_t[a] = b
                    mapping_t_to_s[b] = a
                else:
                    return False
            else:
                if mapping_s_to_t[a] != b:
                    return False
        return True

