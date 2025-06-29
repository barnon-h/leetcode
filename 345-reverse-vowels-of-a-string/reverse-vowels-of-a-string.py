class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U']
        chars = [ *s ]
        ups = [*(s.upper())]
        p1 = 0
    
        p2 = len( chars ) - 1

        while p2 > p1:
            if ups[p1] in vowels and ups[ p2 ] in vowels:
                chars[p1], chars[ p2 ] = chars[ p2 ], chars[ p1 ]
                p2 -= 1
                p1 += 1
            
            else:
                if ups[ p2 ] not in vowels: p2 -= 1
                if ups[ p1 ] not in vowels: p1 += 1
        ret = ""
        for i in chars: ret += i
        return ret
            
        