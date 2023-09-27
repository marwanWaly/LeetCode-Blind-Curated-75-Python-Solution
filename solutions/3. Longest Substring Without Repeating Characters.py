class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        hash_map = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in hash_map and l <= hash_map[s[r]]:
                l = hash_map[s[r]] + 1
            else:
                res = max(res, r - l + 1)
            hash_map[s[r]] = r
        return res
