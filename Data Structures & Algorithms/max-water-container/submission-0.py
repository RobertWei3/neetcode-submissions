class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        max_contain = 0
        i, j = 0, len(heights) - 1

        while i < j:
            curr_contain = (j - i) * min(heights[i], heights[j])
            max_contain = max(max_contain, curr_contain)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_contain

