class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        all_combination = []
        min_val = min(candidates)
        def find_combination(curr_list, val):
            if val >= min_val:
                for x in candidates:
                    if x <= val and (len(curr_list) == 0 or (curr_list[-1] <= x)):
                        find_combination(curr_list + [x], val - x)
            else:
                if val == 0:
                    all_combination.append(curr_list)
        find_combination([], target)
        return all_combination
