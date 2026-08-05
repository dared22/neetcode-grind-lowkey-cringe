class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_map = {}
        window = {}
        l = 0
        best = ()
        for char in t:
            t_map[char] = 1 + t_map.get(char, 0)
        have, need = 0, len(t_map)

        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen  != float("infinity") else ""

            

            
        
            
        
