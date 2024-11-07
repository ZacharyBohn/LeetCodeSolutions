# my first solution
# this one fails on time
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n) time and space
        #
        # mapping of
        # n: index of n
        hashset = {nums[y]: y for y in range(len(nums))}
        # mapping of
        # min answer: [max answer]
        duplicates = set()
        answers = []

        # O(n^2) time and O(1) space
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                # skip duplicate of i and j
                if i == j:
                    continue
                z = -(x+y)
                k = hashset.get(z, None)
                # skip if no possible answer exists
                if not k:
                    continue
                # skip if k is a duplicate of i or j
                if k == i or k == j:
                    continue
                # found a valid answer
                minimum = min(x, y, z)
                maximum = max(x, y, z)
                if (minimum, maximum) in duplicates:
                    continue
                duplicates.add((minimum, maximum))
                answers.append([x, y, z])
        return answers

# second solution using more clever maths
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answers = []
        duplicates = set()

        # count how many of each element there are
        counts = {}
        for n in nums:
            value = counts.get(n, 0)
            counts[n] = value + 1

        # O(n^2) time and O(1) space
        for x in counts:
            for y in counts:
                # not enough elements
                if x == y and counts[x] == 1:
                    continue
                z = -(x+y)
                z_count = counts.get(z, None)
                # z doesn't exist, so x,y pair can't be an answer
                if not z_count:
                    continue
                # not enough elements
                if z_count == 1 and (z == x or z == y):
                    continue
                # not enough elements
                if z_count == 2 and (z == x and z == y):
                    continue
                dupe = (min(x,y,z), max(x,y,z))
                # this answer has already been recorded
                if dupe in duplicates:
                    continue
                answers.append([x, y, z])
                duplicates.add(dupe)
        return answers


 class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        for x in counts:
            for y in counts:
                z = -(x+y)
                if not counts.get(z, None):
                    continue
                if counts[x] == 1 and (x == y or x == z):
                    continue
                if counts[y] == 1 and y == z:
                    continue
                if counts[x] == 2 and x == y and y == z:
                    continue
                solutions.add(tuple(sorted([x,y,z])))
        return list(solutions)

