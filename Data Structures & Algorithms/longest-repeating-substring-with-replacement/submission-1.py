class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        char_dict = {}
        maxf = 0
        for r in range(len(s)):
            char_dict[s[r]] = 1 + char_dict.get(s[r], 0)
            maxf = max(maxf, char_dict[s[r]])
            
            while r - l + 1 - maxf  > k:
                char_dict[s[l]] -= 1
                l += 1

            best = max(r-l+1, best)

        return best


        
        
       
