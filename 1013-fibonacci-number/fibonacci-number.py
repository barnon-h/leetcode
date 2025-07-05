class Solution:
    d = {}

    def fib( self, n: int ) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n in self.d.keys(): return self.d[ n ]
        
        self.d[ n ] = self.fib( n - 1 ) + self.fib( n - 2 )
        return self.d[ n ] 
        