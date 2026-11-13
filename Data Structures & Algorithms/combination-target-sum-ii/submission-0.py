class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            val = candidates[index]
            subset.append(val)
            backtrack(index+1, subset, total + val)
            subset.pop()

            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                index += 1

            backtrack(index+1, subset, total)
        
        backtrack(0, [], 0)

        return result