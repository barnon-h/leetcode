class Solution:
    def mergeAlternately( self, word1: str, word2: str ) -> str:
        
        w1_l = len( word1 )
        w2_l = len( word2 )
        
        ret = ""
        
        final_len = max([ w1_l, w2_l ])
        
        for i in range( final_len ):
            if i < w1_l: ret += word1[ i ]
            if i < w2_l: ret += word2[ i ]
        return ret

        