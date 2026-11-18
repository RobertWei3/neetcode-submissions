class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        Ifdup = {}
        l = 0
        max_count = 0

        for r in range(len(s)):
            if s[r] in Ifdup:
                # l = r
                l = max(Ifdup[s[r]] + 1, l)
                # Ifdup.clear()
            Ifdup[s[r]] = r
            max_count = max(max_count, r-l+1)

        return max_count


