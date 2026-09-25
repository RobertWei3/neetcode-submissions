class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1

        while l < r:
            sumUp = numbers[l] + numbers[r]

            if sumUp < target:
                l += 1
            if sumUp > target:
                r -= 1
            if sumUp == target:
                return [l+1, r+1]
        return []

            