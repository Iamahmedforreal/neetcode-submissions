class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for s in i:
                count[ord(s) - ord('a')]+=1
            seen[tuple(count)].append(i)
        return list(seen.values()) 
        
     

        

        

        
      
            





    
