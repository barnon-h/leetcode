class Solution:
    def mergeAlternately( self, word1: str, word2: str ) -> str:
        ret = ""
        final_len = len( word1 ) if len( word1 ) > len( word2 ) else len( word2 )
        for i in range( final_len ):
            if i < len( word1 ): ret += word1[ i ]
            if i < len( word2 ): ret += word2[ i ]
        return ret

        