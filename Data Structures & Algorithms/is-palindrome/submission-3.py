class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s = "".join(char for char in s if char.isalnum())
        # 不要这么创建s，空间复杂度会变为n
        i, j = 0, len(s) -1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            
        return True

