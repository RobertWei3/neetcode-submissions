class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     if nums[i] + nums[j] > target:
        #         j -= 1
        #     elif nums[i] + nums[j] < target:
        #         i += 1
        #     else:
        #         return [i,j]
        # return []

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        return []


