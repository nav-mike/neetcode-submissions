class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers)
        s = sum(numbers[index1:index2])

        while s != target:
            if s > target:
                index2 -= 1
            else:
                index1 += 1
            s = sum(numbers[index1:index2])
        
        return [index1+1, index2]
