class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            complimenter_number = target - num
            if complimenter_number in seen:
                return[seen[complimenter_number] , i]
            seen[num] = i
        return []
            
        
        
        