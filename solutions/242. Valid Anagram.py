class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_freq = {}
        t_freq = {}
        
        for c1, c2 in zip(s, t):
            s_freq[c1] = 1 + s_freq.get(c1, 0)
            t_freq[c2] = 1 + t_freq.get(c2, 0)
        
        for k in s_freq:
            s_freq_val = s_freq.get(k, None)
            t_freq_val = t_freq.get(k, None)
            if not (s_freq_val and t_freq_val and s_freq_val == t_freq_val):
                return False

        return True
