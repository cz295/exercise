class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    item = stack.pop(-1)
                    if item != match_dict[i]:
                        return False
        if len(stack) > 0:
            return False
        else:
            return True
