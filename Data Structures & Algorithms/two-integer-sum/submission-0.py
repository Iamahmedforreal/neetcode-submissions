class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i , j in enumerate(nums):
            compatible_value = target - j
            if compatible_value in seen:
                return[seen[compatible_value] , i]
            seen[j] = i
        return []
        