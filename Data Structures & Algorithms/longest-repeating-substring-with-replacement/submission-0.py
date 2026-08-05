class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        char_dict = {}

        for r in range(len(s)):
            if s[r] not in char_dict:
                char_dict[s[r]] = 1
            else:
                char_dict[s[r]] += 1

            most_frequent_num = sorted(list(char_dict.values()), reverse=True)[0]

            while r - l + 1 - most_frequent_num  > k:
                char_dict[s[l]] -= 1
                l += 1

            best = max(r-l+1, best)

        return best


        
        
       
