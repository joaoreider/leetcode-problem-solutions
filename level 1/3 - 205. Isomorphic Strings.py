

# My solution: (59ms)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        aux = {}
        sl = list(s)
        
        for i in range(len(s)):
        
            if sl[i] not in aux:

                if t[i] not in aux.values():
                    aux[sl[i]] = t[i] 
            
            else:
                
                aux[sl[i]+str(i)] = aux[sl[i]]
        

        return list(aux.values()) == list(t)


# Best solution: (15ms)      
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False    
            elif t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]
        return True
