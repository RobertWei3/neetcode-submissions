import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points:
            d = x**2 + y**2

            heapq.heappush(h, (-d, x, y))
            if len(h) > k:
                heapq.heappop(h)

        return [t[1:] for t in h]


