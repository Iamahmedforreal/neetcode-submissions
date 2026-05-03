class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            chS = s[i]
            chT = t[i]

            if chS in countS:
                countS[chS]+=1
            else:
                countS[chS] = 1
            if chT in countT:
                countT[chT]+=1
            else:
                countT[chT] = 1
        
        return countS == countT
           


        