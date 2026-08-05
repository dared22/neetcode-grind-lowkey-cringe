class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_lst = []
        l,r = 0, len(s1)
        while r <= len(s2):
            cut = s2[l:r]
            print(cut)
            if sorted(s1) == sorted(cut):
                return True
            else:
                l += 1
                r += 1
        return False

