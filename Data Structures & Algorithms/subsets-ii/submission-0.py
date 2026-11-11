class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, subset):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            val = nums[index]
            subset.append(val)
            backtrack(index+1, subset)
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            backtrack(index+1, subset)
        
        backtrack(0, [])

        return result