class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        curr_len = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                curr_len = 1
                l = x + 1
                while l in nums_set:
                    curr_len += 1
                    l += 1
                max_len = max(curr_len, max_len)
        return max_len  

        
        
#         visited = {i: 0 for i in nums}
#         max_len = 0
#         curr_len = 0

#         def add_len(x):
#             # print(x)
#             nonlocal max_len
#             nonlocal curr_len
#             curr_len += 1
#             visited[x] = 1
#             max_len = max(curr_len, max_len)
#             if x - 1 in visited and visited[x - 1] == 0:
#                 add_len(x - 1)
#             if x + 1 in visited and visited[x + 1] == 0:
#                 add_len(x + 1)

#         for x in visited:
#             if visited[x] == 0:
#                 curr_len = 0
#                 add_len(x)
#         return max_len


