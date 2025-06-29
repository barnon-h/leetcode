class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U']
        chars = [ *s ]
        p1 = 0
    
        p2 = len( chars ) - 1

        while p2 > p1:
            if chars[p1].upper() in vowels and chars[ p2 ].upper() in vowels:
                chars[p1], chars[ p2 ] = chars[ p2 ], chars[ p1 ]
                p2 -= 1
                p1 += 1
            
            else:
                if chars[ p2 ].upper() not in vowels: p2 -= 1
                if chars[ p1 ].upper() not in vowels: p1 += 1
        ret = ""
        for i in chars: ret += i
        return ret
            
        