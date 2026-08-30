class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            sort_item = "".join(sorted(i))
            if sort_item not in seen:
                seen[sort_item] = []
            seen[sort_item].append(i)
        return list(seen.values())


        
     

        

        

        
      
            





    
