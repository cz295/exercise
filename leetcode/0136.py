class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for i in nums:
            ret ^= i
        return ret
    
        from collections import defaultdict
        _dict = defaultdict(int)
        for i in nums:
            _dict[i] += 1
        for i in _dict:
            if _dict[i] == 1:
                return i
        
