class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountS = {}
        countT = {}

        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i] , 0)
            countT[t[i]] = 1 + countT.get(t[i] , 0)
        return CountS == countT

    


        
            
            


       
           


        