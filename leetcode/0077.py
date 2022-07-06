class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_combinations = []
        # in_list = set()

        def get_combination(_list, _k):
            # print(_list, _k)
            if len(_list) == k:
                all_combinations.append(_list.copy())
            else:
                for x in range(_k + 1, n + 1):
                    _list.append(x)
                    get_combination(_list, x)
                    _list.pop()

        get_combination([], 0)
        return all_combinations
        
#         all_combinations = []
#         in_list = set()

#         def get_combination(_list):
#             # print(_list)
#             if len(_list) == k:
#                 all_combinations.append(_list.copy())
#             else:
#                 for x in range(1, 1 + n):
#                     if x not in in_list and (not _list or x > _list[-1]):
#                         _list.append(x)
#                         in_list.add(x)
#                         get_combination(_list)
#                         in_list.remove(x)
#                         _list.pop()
#         get_combination([])
#         return all_combinations
