class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        most_frequent = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
        return list(most_frequent.keys())[:k]