class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = {key: 0 for key in set(nums)}
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1

        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # for num in nums:
        #     if num in res:
        #         res[num] +=1
        return sorted(res, key=res.get, reverse=True)[:k]
