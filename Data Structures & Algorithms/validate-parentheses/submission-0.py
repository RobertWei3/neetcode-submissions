class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []

        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in mapping:
                top_element =  valid_stack.pop() if valid_stack else "#"

                if mapping[c] != top_element:
                    return False
            else:
                valid_stack.append(c)
        return len(valid_stack) == 0