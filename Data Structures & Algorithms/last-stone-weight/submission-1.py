import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            first_biggest = -heapq.heappop(h)
            second_biggest = -heapq.heappop(h)

            if first_biggest != second_biggest:
                heapq.heappush(h, second_biggest - first_biggest)

        return -h[0] if h else 0
