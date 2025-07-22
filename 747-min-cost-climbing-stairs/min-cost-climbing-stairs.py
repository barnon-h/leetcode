class Solution:

    d = {}

    def minCostClimbingStairs( self, cost: List[ int ]) -> int:
        self.d = {}
        return self.helper( 0, cost )

    def helper( self, idx : int, cost : List[ int ]) -> int:
        l = len( cost )
        if l - idx == 1:
            return 0
        elif l - idx == 2:
            return min( cost[ idx ], cost[ idx + 1 ])
        else:
            if idx not in self.d:
                self.d[idx]  = cost[ idx ] + self.helper( idx + 1, cost )
            if idx + 1 not in self.d:
                self.d[idx + 1] = cost[ idx + 1 ] + self.helper( idx + 2,cost )

            return min([ self.d[ idx ], self.d[ idx + 1 ]])        