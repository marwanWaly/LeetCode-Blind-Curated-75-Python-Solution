class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        count_t, window = {}, {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        
        have, need = 0, len(count_t)
        l = 0
        res, res_len = (-1, -1), float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                new_c = s[l]
                curr_len = r - l + 1
                # update the results
                if curr_len < res_len:
                    res, res_len = (l , r), curr_len
                
                window[new_c] -= 1
                if new_c in count_t and window[new_c] < count_t[new_c]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l : r+1] if l != -1 else ""
