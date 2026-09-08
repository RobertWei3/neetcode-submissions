import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            first_biggest = -heapq.heappop(h)
            second_biggest = -heapq.heappop(h)

            heapq.heappush(h, second_biggest - first_biggest)

        return -h[0]
