class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEatAll(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)

            return hours <= h


        while l < r:
            mid = (l + r) // 2

            if canEatAll(mid):
                r = mid
            else:
                l = mid + 1

        return l