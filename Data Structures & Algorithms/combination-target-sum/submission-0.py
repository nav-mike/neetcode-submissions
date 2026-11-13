class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            
            if index >= len(nums) or total > target:
                return
            
            for i in range(index, len(nums)):
                if total + nums[i] > target:
                    return
                
                subset.append(nums[i])
                backtrack(i, subset, total + nums[i])
                subset.pop()

        backtrack(0, [], 0)

        return result