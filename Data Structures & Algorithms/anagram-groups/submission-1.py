class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in my_dict.keys():
                my_dict.setdefault(key, []).append(word)
            else:
                my_dict[key] = []
                my_dict[key].append(word)
        return list(my_dict.values())