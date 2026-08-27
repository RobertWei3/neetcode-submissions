class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))

        max_count, curr = 1, 1
        i, j = 0, 1

        while j < len(nums):
            if nums[j] - nums[i] == 1:
                curr +=1
            else:
                curr = 1
            max_count = max(max_count, curr)
            j += 1
            i += 1
        return max_count