from typing import List

class Solution1:
	def longestConsecutive(self, nums: List[int]) -> int:
		hashset = set(nums)
		longest_seq = 0
		for n in nums:
			if n-1 in hashset: continue
			current_seq = 1
			while n+1 in hashset:
				current_seq += 1
				n += 1
			longest_seq = max(longest_seq, current_seq)
		return longest_seq


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = {}
        longest = 0
        for n in nums:
            if n in hashset: continue
            start, end = n, n
            if n-1 in hashset: start = hashset[n-1][0]
            if n+1 in hashset: end = hashset[n+1][1]
            # to be able to skip duplicates of n
            hashset[n] = None
            hashset[start] = [start, end]
            hashset[end] = [start, end]
            longest = max(longest, end - start + 1)
        return longest