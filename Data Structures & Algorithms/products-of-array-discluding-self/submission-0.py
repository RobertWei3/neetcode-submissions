import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left_prod, right_prod = 1, 1
        for i in range(len(nums)):
            left = math.prod(nums[:i]) * left_prod
            right = math.prod(nums[i+1:]) * right_prod
            res.append(left* right)

        return res


        