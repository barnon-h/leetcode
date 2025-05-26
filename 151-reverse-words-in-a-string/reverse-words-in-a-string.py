class Solution:
    from collections import deque

    def reverseWords(self, s: str) -> str:
        pq = deque()

        word = ""
        for i in s:
            if i != " ":
                word += i
            else:
                if word.strip()!= "":
                    pq.append(word)
                word = ""
        pq.append(word)

        ret = ""
        for _ in range(len(pq)):
            ret += pq.pop() + " "

        return ret.strip()

        
            
            