import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            left = math.prod(nums[:i]) 
            right = math.prod(nums[i+1:]) 
            res.append(left* right)

        return res


        