class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        g = max( candies )
        return [ i + extraCandies >= g for i in candies]