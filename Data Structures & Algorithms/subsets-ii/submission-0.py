class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        passs = []

        def dfs(i):
            if i >= len(nums):
                res.append(passs.copy())
                return

            # decide to inclue the num
            passs.append(nums[i])
            dfs(i+1)
            passs.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            dfs(i+1)
        
        dfs(0)
        return res