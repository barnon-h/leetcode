class Solution:
    d = {}
    def canJump(self, nums: List[ int ]) -> bool:
        self.d = {}
        return self.helper( nums )
        

    def helper( self, n: List[ int ], idx : int = 0 ) -> bool:
        if idx == len( n ) - 1:
            return True
        
        elif idx >= len( n ):
            return False
        
        elif n[ idx ] <= 0:
            return False
        
        else:
            ret = False 
            
            for i in range( n[ idx ] , 0, -1 ):
                if idx + i not in self.d:
                    self.d[ idx+i ] = self.helper( n, idx + i )
                
                if self.d[idx+i] is True: 
                    ret = True
                    break
            return ret
