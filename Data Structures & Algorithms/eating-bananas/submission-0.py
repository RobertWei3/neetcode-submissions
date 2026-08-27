class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            total_time = 0 

            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
                