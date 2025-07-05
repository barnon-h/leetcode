class Solution:

    d = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if n in self.d.keys():
                return self.d[ n ]
            else:
                self.d[ n ] = self.climbStairs( n - 2 ) + self.climbStairs( n - 1 )
                return self.d[ n ]


        