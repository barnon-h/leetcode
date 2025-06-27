class Solution:
    def is_valid( self, i:int, a:List )-> bool:
        l = i - 1 < 0 or a[i-1] == 0
        r = i >= len(a)-1 or a[i+1] == 0
        m = a[i] == 0
        return r and l and m
        
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        z,i = 0,0
        while i < len(flowerbed):
            if self.is_valid(i, flowerbed):
                z+=1
                i += 1
            i += 1
        return n <= z
        