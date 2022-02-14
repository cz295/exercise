class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        i1, i2 = 0, len(s) - 1
        while i1 < i2:
            if s[i1] != s[i2]:
                break
            else:
                i1 += 1
                i2 -= 1
        if i1 < i2:
            cnt = 0
            for i1_new, i2_new in ((i1 + 1, i2), (i1, i2 - 1)):
                while i1_new < i2_new:
                    if s[i2_new] != s[i1_new]:
                        cnt += 1
                        break
                    else:
                        i2_new -= 1
                        i1_new += 1
            if cnt == 2:
                return False
            else:
                return True
        else:
            return True
