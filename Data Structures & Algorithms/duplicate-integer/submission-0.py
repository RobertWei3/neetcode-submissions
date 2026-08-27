class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_set = []
        for num in nums:
            if num in empty_set:
                return True
            else:
                empty_set.append(num)
        return False