class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = random.choice(nums)
        left  = [i for i in nums if i < x]
        mid   = [i for i in nums if i == x]
        right = [i for i in nums if i > x]

        r, m = len(right), len(mid)
        if k <= r:
            return self.findKthLargest(right, k)
        elif k > r + m:
            return self.findKthLargest(left, k - r - m)
        else:
            return mid[0]
