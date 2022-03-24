# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in temp:
                return [temp[diff], i]
            else:
                temp[n] = i
