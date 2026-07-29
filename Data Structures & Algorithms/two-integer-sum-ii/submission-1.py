class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1
        
        while index1 < index2:
            s = numbers[index1] + numbers[index2]
            if s > target:
                index2 -= 1
            elif s < target:
                index1 += 1
            else:
                return [index1+1, index2+1]
        
        return []
