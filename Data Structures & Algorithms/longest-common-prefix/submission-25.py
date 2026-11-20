class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        l =""
       
        z=strs[0]
        for i in strs : 
            if len (i) < len (z) : 
                z = i
        s=0        
        for y in range (len(z)) :     
            for b in strs : 
                if b[s] != z[s] :  
                    return l 
                
            l = l + z[s]
            s = s+1 
        return l