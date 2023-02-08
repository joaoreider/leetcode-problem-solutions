
# My solution: (31ms)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        aux = ''
        tam_t = len(t) 
        inicio = 0

        for k in s:
            if inicio == tam_t:
                break
            for c in range(inicio, tam_t):
                
                if k == t[c]:

                    aux += t[c]
                    inicio = c+1
                    break
            
        #print(s)
        #print(aux)
        return True if s == aux else False




#Best solution: (11ms)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i = 0
        for ch in t:
            if i <= len(s)-1:
                if ch == s[i]:
                    i += 1
        return i == len(s)