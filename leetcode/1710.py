class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_unit = 0
        remain_size = truckSize
        for no_box, unit_per_box in boxTypes:
            if remain_size > no_box:
                max_unit += no_box * unit_per_box
                remain_size -= no_box
            else:
                max_unit += remain_size * unit_per_box
                break
        return max_unit
            
            
