class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        curr = 0
        while curr <= len(flowerbed) - 1:
            prev = 0 if curr == 0 else flowerbed[curr - 1]
            if prev == 0 and flowerbed[curr] == 0:
                if curr == len(flowerbed) - 1:
                    cnt += 1
                    curr += 1
                elif flowerbed[curr + 1] == 0:
                    cnt += 1
                    curr += 2
                else:
                    curr += 3
                    
            else:
                curr += 1
            if cnt >= n:
                return True
        return False
