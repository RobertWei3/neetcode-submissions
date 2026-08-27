class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers) - 1):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

        l, r = 0, len(numbers) -1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            
            if curr_sum == target:
                return [l+1, r+1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1