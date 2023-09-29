class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for c in s:
            if c in hash_map:
                if stack and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
