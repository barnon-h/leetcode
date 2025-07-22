class Solution:
    
    d = {}
    
    def rob(self, nums: List[ int ]) -> int:
        self.d = {}
        return self.helper( 0, nums )

    def helper( self, idx : int, nums : List[ int ] ) -> int:
        if idx >= len( nums ): 
            return 0

        elif len( nums ) - idx == 1:
            return nums[ idx ]
        
        elif len( nums ) - idx == 2:
            return max([ nums[ idx ], nums[ idx + 1 ]])

        else:
            if idx not in self.d:
                self.d[ idx ] = nums[ idx ] + self.helper( idx + 2, nums )
            
            if idx+1 not in self.d:
                self.d[ idx + 1 ] = nums[ idx + 1 ] + self.helper( idx + 3, nums )

            return max([ self.d[ idx ], self.d [idx + 1 ]]) 


        