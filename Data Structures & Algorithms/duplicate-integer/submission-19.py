class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
                seen = {}
                for nums in nums:
                        if nums in seen:
                                return True
                        seen[nums] = True
                return False

                
              
        
        