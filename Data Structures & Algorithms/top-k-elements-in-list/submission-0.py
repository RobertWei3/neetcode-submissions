class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {key: 0 for key in set(nums)}
        for num in nums:
            if num in res:
                res[num] +=1
        return sorted(res, key=res.get, reverse=True)[:k]
