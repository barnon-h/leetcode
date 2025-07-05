class Solution:
    
    d = {}

    def tribonacci( self, n: int ) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        if n in self.d.keys(): return self.d[ n ]

        self.d[ n ] = sum([ self.tribonacci( n - i ) for i in range( 1, 4 )])

        return self.d[ n ]
        